import sys
import time
import datetime as dt
import math
from serial.tools import list_ports
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from _gui.mainwindow import Ui_MainWindow
from _core.E22 import E22, Config
from _func.styler import styler

loradev: E22 | None = None
cfg = Config()
barray: bytearray = bytearray()
start: float | None = None
logfile: str = ''

def show_error(in1, in2, in3):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setWindowTitle(f"{in1}")
    msg_box.setText(f"Ошибка! {in2}")
    QtCore.QTimer.singleShot(3000, msg_box.close)
    msg_box.exec()

class PingThread(QtCore.QThread):

    ping = QtCore.Signal(bytearray)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        self._running = True
        self.core_work()

    def core_work(self):
        while self._running:
            loradev.send(b'6<+>>ping')
            if loradev.ser.in_waiting > 0:
                inbytes = loradev.recv()
                if b'>>ping' in inbytes:
                    self.ping.emit(inbytes)
            else:
                self.ping.emit(b'8<+>>empty!')
            QtCore.QThread.sleep(1)

    def stop(self):
        self._running = False

class RxThread(QtCore.QThread):

    message = QtCore.Signal(bytearray)
    waiting = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        self._running = True
        self.core_work()

    def core_work(self):
        global barray
        while self._running:
            QtCore.QThread.sleep(1)
            if loradev.ser.in_waiting > 0:
                inbytes = loradev.recv()
                if b'<$' in inbytes or b'>>ping' in inbytes:
                    barray.extend(inbytes)
                    self.message.emit(barray)
                else:
                    barray.extend(inbytes)
                    self.waiting.emit()

    def stop(self):
        self._running = False

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('E22-Messenger')

        self.rxthread = RxThread()
        self.rxthread.message.connect(self.updaterx)
        self.rxthread.waiting.connect(self.pauserx)
        self.pingthread = PingThread()
        self.pingthread.ping.connect(self.updateping)

        self.b_refr.clicked.connect(self.refresh)
        self.b_connect.clicked.connect(self.loraconnect)
        self.b_edit.clicked.connect(self.editconf)
        self.b_reset.clicked.connect(self.reset)
        self.b_message.clicked.connect(self.sendtext)
        self.b_ping.clicked.connect(self.sendping)
        self.b_clear.clicked.connect(self.clear)
        self.b_file.clicked.connect(self.scroll)

    def refresh(self):
        ports = list_ports.comports()
        if ports != [] and self.cmb_port.currentText() == '':
            for port in ports:
                self.cmb_port.addItem(port.device)

    def loraconnect(self):
        global loradev, cfg, logfile
        port = self.cmb_port.currentText()
        match self.b_connect.isChecked():
            case True:
                if len(port) != 0:
                    loradev = E22(port)
                    logfile = 'logs/'+f'{str(dt.datetime.now())[0:-10]}.log'.replace(' ','_').replace(':','-')
                    with open(logfile, 'w', encoding='utf-8') as file:
                        file.write(f'--- Started message logging at {str(dt.datetime.now())[0:-7]} --- \n')
            case False:
                if loradev is not None:
                    self.rxthread.terminate()
                    self.pingthread.terminate()
                    loradev.close()
                    loradev = None
                    cfg = Config()

    def editconf(self):
        global loradev, cfg
        if loradev is not None:
            self.rxthread.terminate()
            self.pingthread.terminate()
            cfg.set_all(loradev.config_get())
            cfg.set_software_mode_switching(enable=True)
            cfg.set_serial_baud(int(9600))
            cfg.set_wireless_speed(5)
            cfg.set_packet_size(64)
            cfg.set_transmitting_power(int(self.cmb_pow.currentIndex()))
            cfg.set_channel(self.sp_chan.value())
            cfg.set_netid(self.sp_id.value())
            loradev.config_set(cfg.get_all())
            loradev.software_mode_switch('transmission')
            self.rxthread.start()

    def reset(self):
        global loradev, barray
        if loradev is not None:
            loradev.ser.reset_input_buffer()
            loradev.ser.reset_input_buffer()
            barray.clear()
            self.gr_rx.setEnabled(True)

    def sendtext(self):
        if loradev is not None:
            message = '$>' + self.txt_tx.toPlainText() + '<$'
            pack = message.encode()
            sz = len(pack)
            outbytes = str(sz).encode()+b'<+'+pack
            # print(sz)
            buff = 64
            # vol = 0
            self.setCursor(QtCore.Qt.CursorShape.WaitCursor)
            if sz > buff:
                self.rxthread.terminate()
                for i in range(math.ceil(sz/buff)):
                    loradev.send(outbytes[buff*i:buff*i+buff])
                    time.sleep(0.15)
                self.rxthread.start()
            else:
                loradev.send(outbytes)
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            curtext =  self.txt_rx.toPlainText()
            a = message.replace('$>', '')
            b = a.replace('<$', '')
            dstr = str(dt.datetime.now())[0:-7]
            self.txt_tx.clear()
            self.txt_rx.setText(f'{curtext} \n'
                                f'--- {dstr} Sended: \n'
                                f'{b} \n'
                                '--- \n')
            with open(logfile, 'a', encoding='utf-8') as file:
                file.write(f'{curtext} \n'
                            f'--- {dstr} Sended: \n'
                            f'{b} \n'
                            '--- \n')
            self.txt_rx.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def sendping(self):
        if loradev is not None:
            match self.b_ping.isChecked():
                case False:
                    self.pingthread.terminate()
                    self.rxthread.start()
                case True:
                    self.rxthread.terminate()
                    self.pingthread.start()

    def updaterx(self, inp):
        global barray, start
        curtext =  self.txt_rx.toPlainText()
        message = inp.decode().split('<+')
        rxsize = len(message[1].encode())
        txsize = int(message[0].replace('<+',''))
        barray.clear()
        a = message[1].replace('$>', '')
        b = a.replace('<$', '')
        dstr = str(dt.datetime.now())[0:-7]
        self.gr_rx.setEnabled(True)
        self.txt_rx.setText(f'{curtext} \n'
                            f'--- {dstr} Received: \n'
                            f'{b} \n'
                            '--- \n')
        with open(logfile, 'a', encoding='utf-8') as file:
            file.write(f'{curtext} \n'
                        f'--- {dstr} Received: \n'
                        f'{b} \n'
                        '--- \n')
        self.txt_rx.moveCursor(QtGui.QTextCursor.MoveOperation.End)
        if start is not None:
            self.txt_control.setText(f'--- {dstr} \n'
                                     '\n'
                                     f'Received: {rxsize} Bytes; \n'
                                     f'Lost: {txsize-rxsize} Bytes; \n'
                                     f'Transmission time: {round(time.time()-start,2)} s.')
            start = None
        else:
            self.txt_control.setText(f'--- {dstr} \n'
                                     '\n'
                                     f'Received: {rxsize} Bytes; \n'
                                     f'Lost: {txsize-rxsize} Bytes. \n')

    def pauserx(self):
        global start
        if start is None:
            start = time.time()
        dstr = str(dt.datetime.now())[0:-7]
        self.gr_rx.setEnabled(False)
        self.txt_control.setText(f'--- {dstr} \n'
                                 '\n'
                                 'Receiving a message...')

    def updateping(self, inp):
        dstr = str(dt.datetime.now())[0:-7]
        message = inp.decode().split('<+')
        self.txt_control.clear()
        self.txt_rx.setText(f'--- {dstr} \n'
                            f'{message[1]} \n'
                            '--- \n')

    def clear(self):
        self.txt_rx.clear()
        self.txt_control.clear()

# sys.excepthook = show_error

if not QApplication.instance():
    app = QApplication(sys.argv)
else:
    app = QApplication.instance()

styler(app)

lw = MainWindow()
lw.show()

sys.exit(app.exec())
