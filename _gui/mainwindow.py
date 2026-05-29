from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QGroupBox,
    QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gr_con = QGroupBox(self.centralwidget)
        self.gr_con.setObjectName(u"gr_con")
        self.gridLayout_4 = QGridLayout(self.gr_con)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(7)
        # self.gridLayout_4.setContentsMargins(6, 10, 6, 10)
        self.label = QLabel(self.gr_con)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.cmb_port = QComboBox(self.gr_con)
        self.cmb_port.setObjectName(u"cmb_port")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_port.sizePolicy().hasHeightForWidth())
        self.cmb_port.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.cmb_port, 0, 1, 1, 1)

        self.b_refr = QPushButton(self.gr_con)
        self.b_refr.setObjectName(u"b_refr")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_refr.sizePolicy().hasHeightForWidth())
        self.b_refr.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.b_refr, 1, 0, 1, 1)

        self.b_connect = QPushButton(self.gr_con)
        self.b_connect.setObjectName(u"b_connect")
        sizePolicy1.setHeightForWidth(self.b_connect.sizePolicy().hasHeightForWidth())
        self.b_connect.setSizePolicy(sizePolicy1)
        self.b_connect.setCheckable(True)

        self.gridLayout_4.addWidget(self.b_connect, 1, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 2)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)

        self.gridLayout_3.addWidget(self.gr_con, 0, 2, 1, 1)

        self.gr_set = QGroupBox(self.centralwidget)
        self.gr_set.setObjectName(u"gr_set")
        self.gridLayout_2 = QGridLayout(self.gr_set)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(7)
        # self.gridLayout_2.setContentsMargins(6, 10, 6, 6)
        self.cmb_pow = QComboBox(self.gr_set)
        self.cmb_pow.addItem("")
        self.cmb_pow.addItem("")
        self.cmb_pow.addItem("")
        self.cmb_pow.addItem("")
        self.cmb_pow.setObjectName(u"cmb_pow")
        sizePolicy.setHeightForWidth(self.cmb_pow.sizePolicy().hasHeightForWidth())
        self.cmb_pow.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.cmb_pow, 0, 1, 1, 1)

        self.label_26 = QLabel(self.gr_set)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 1, 0, 1, 1)

        self.b_edit = QPushButton(self.gr_set)
        self.b_edit.setObjectName(u"b_edit")
        sizePolicy1.setHeightForWidth(self.b_edit.sizePolicy().hasHeightForWidth())
        self.b_edit.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.b_edit, 3, 0, 1, 3)

        self.label_24 = QLabel(self.gr_set)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)

        self.sp_id = QSpinBox(self.gr_set)
        self.sp_id.setObjectName(u"sp_id")
        sizePolicy1.setHeightForWidth(self.sp_id.sizePolicy().hasHeightForWidth())
        self.sp_id.setSizePolicy(sizePolicy1)
        self.sp_id.setValue(1)

        self.gridLayout_2.addWidget(self.sp_id, 2, 1, 1, 1)

        self.label_25 = QLabel(self.gr_set)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_25, 0, 2, 1, 1)

        self.label_27 = QLabel(self.gr_set)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 2, 0, 1, 1)

        self.sp_chan = QSpinBox(self.gr_set)
        self.sp_chan.setObjectName(u"sp_chan")
        sizePolicy1.setHeightForWidth(self.sp_chan.sizePolicy().hasHeightForWidth())
        self.sp_chan.setSizePolicy(sizePolicy1)
        self.sp_chan.setMaximum(64)

        self.gridLayout_2.addWidget(self.sp_chan, 1, 1, 1, 1)

        self.b_reset = QPushButton(self.gr_set)
        self.b_reset.setObjectName(u"b_reset")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_reset.sizePolicy().hasHeightForWidth())
        self.b_reset.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.b_reset, 4, 0, 1, 3)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout_3.addWidget(self.gr_set, 1, 2, 1, 1)

        self.gr_tx = QGroupBox(self.centralwidget)
        self.gr_tx.setObjectName(u"gr_tx")
        self.gridLayout = QGridLayout(self.gr_tx)
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_message = QPushButton(self.gr_tx)
        self.b_message.setObjectName(u"b_message")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.b_message.sizePolicy().hasHeightForWidth())
        self.b_message.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.b_message, 1, 0, 1, 2)

        self.txt_tx = QTextEdit(self.gr_tx)
        self.txt_tx.setObjectName(u"txt_tx")

        self.gridLayout.addWidget(self.txt_tx, 0, 0, 1, 2)

        self.b_file = QPushButton(self.gr_tx)
        self.b_file.setObjectName(u"b_file")
        sizePolicy3.setHeightForWidth(self.b_file.sizePolicy().hasHeightForWidth())
        self.b_file.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.b_file, 2, 1, 1, 1)

        self.b_ping = QPushButton(self.gr_tx)
        self.b_ping.setObjectName(u"b_ping")
        sizePolicy1.setHeightForWidth(self.b_ping.sizePolicy().hasHeightForWidth())
        self.b_ping.setSizePolicy(sizePolicy1)
        self.b_ping.setCheckable(True)

        self.gridLayout.addWidget(self.b_ping, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 9)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 1)

        self.gridLayout_3.addWidget(self.gr_tx, 0, 1, 3, 1)

        self.gr_rx = QGroupBox(self.centralwidget)
        self.gr_rx.setObjectName(u"gr_rx")
        self.verticalLayout_2 = QVBoxLayout(self.gr_rx)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_rx = QTextBrowser(self.gr_rx)
        self.txt_rx.setObjectName(u"txt_rx")

        self.verticalLayout_2.addWidget(self.txt_rx)

        self.b_clear = QPushButton(self.gr_rx)
        self.b_clear.setObjectName(u"b_clear")
        sizePolicy3.setHeightForWidth(self.b_clear.sizePolicy().hasHeightForWidth())
        self.b_clear.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.b_clear)

        self.verticalLayout_2.setStretch(0, 11)
        self.verticalLayout_2.setStretch(1, 1)

        self.gridLayout_3.addWidget(self.gr_rx, 0, 0, 3, 1)

        self.gr_control = QGroupBox(self.centralwidget)
        self.gr_control.setObjectName(u"gr_control")
        self.verticalLayout = QVBoxLayout(self.gr_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_control = QTextBrowser(self.gr_control)
        self.txt_control.setObjectName(u"txt_control")

        self.verticalLayout.addWidget(self.txt_control)


        self.gridLayout_3.addWidget(self.gr_control, 2, 2, 1, 1)

        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 5)
        self.gridLayout_3.setRowStretch(2, 3)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        # MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.gr_con.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        # self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0440\u0442\u0430", None))
        # self.b_refr.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        # self.b_connect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        # self.gr_set.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        # self.cmb_pow.setItemText(0, QCoreApplication.translate("MainWindow", u"22", None))
        # self.cmb_pow.setItemText(1, QCoreApplication.translate("MainWindow", u"17", None))
        # self.cmb_pow.setItemText(2, QCoreApplication.translate("MainWindow", u"13", None))
        # self.cmb_pow.setItemText(3, QCoreApplication.translate("MainWindow", u"10", None))

        # self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0430\u043b", None))
        # self.b_edit.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        # self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        # self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0411\u043c", None))
        # self.label_27.setText(QCoreApplication.translate("MainWindow", u"ID \u0441\u0435\u0442\u0438", None))
        # self.b_reset.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0431\u0443\u0444\u0435\u0440", None))
        # self.gr_tx.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0434\u0430\u0447\u0430", None))
        # self.b_message.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        # self.txt_tx.setDocumentTitle("")
        # self.b_file.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        # self.b_ping.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c ping", None))
        # self.gr_rx.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        # self.b_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        # self.gr_control.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u043f\u0440\u0438\u0435\u043c\u0430", None))
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gr_con.setTitle(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port number", None))
        self.b_refr.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.b_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.gr_set.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.cmb_pow.setItemText(0, QCoreApplication.translate("MainWindow", u"22", None))
        self.cmb_pow.setItemText(1, QCoreApplication.translate("MainWindow", u"17", None))
        self.cmb_pow.setItemText(2, QCoreApplication.translate("MainWindow", u"13", None))
        self.cmb_pow.setItemText(3, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.b_edit.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"dBm", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Net ID", None))
        self.b_reset.setText(QCoreApplication.translate("MainWindow", u"Clear buffer", None))
        self.gr_tx.setTitle(QCoreApplication.translate("MainWindow", u"Transmission", None))
        self.b_message.setText(QCoreApplication.translate("MainWindow", u"Send message", None))
        self.txt_tx.setDocumentTitle("")
        self.b_file.setText(QCoreApplication.translate("MainWindow", u"Send file", None))
        self.b_ping.setText(QCoreApplication.translate("MainWindow", u"Ping mode", None))
        self.gr_rx.setTitle(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.b_clear.setText(QCoreApplication.translate("MainWindow", u"Clear history", None))
        self.gr_control.setTitle(QCoreApplication.translate("MainWindow", u"Integrity contol", None))
    # retranslateUi
