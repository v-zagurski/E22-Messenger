br1 = 'rgb(255, 255, 255)'  # background
br2 = 'rgb(230, 230, 240)'  # control elements
br21 = 'rgb(163, 173, 198)'  # control elements accent
br3 = 'rgb(95, 138, 180)'  # highlight
br4 = 'rgb(63, 73, 98)'  # accent
br5 = 'rgb(215, 0, 0)'  # alert

st = (
    'QMainWindow { background-color: '
    + br1
    + '; border: 1px solid grey; border-radius: 5px; } '

    'QDialog { background-color: '
    + br1
    + '; border: 1px solid '
    + br2
    + '; border-radius: 5px; }'

    'QGroupBox { border: 2px solid grey; border-radius: 5px; margin-top: 0px; } '
    'QGroupBox[title] { color: black; font-family: "Times New Roman"; font-size: 16px; font-weight: bold; '
    'border: 2px solid grey; border-radius: 5px; margin-top: 8px; } '
    'QGroupBox::title { subcontrol-origin: margin; left: 9px; } '
    'QLabel { color: black; background-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; } '

    'QLineEdit { color: black; background-color: '
    + br1
    + '; selection-background-color: '
    + br3
    + '; selection-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; '
    'border: 1px solid grey; border-radius: 5px; } '

    'QTextBrowser { color: black; background-color: '
    + br1
    + '; selection-background-color: '
    + br3
    + '; selection-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; '
    'border-width: 1px solid grey; border-radius: 5px; } '

    'QTextEdit { color: black; background-color: '
    + br1
    + '; selection-background-color: '
    + br3
    + '; selection-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; '
    'border: 1px solid grey; border-radius: 5px; } '

    'QComboBox { color: black; background-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; '
    'border: 1px solid grey; border-radius: 5px; padding-left: 6px; } '
    'QComboBox::drop-down { border-left: 1px solid grey; width: 20px; background-color: '
    + br2
    + '; border-radius: 5px; } '
    'QComboBox::drop-down:hover { border-left: 1px solid grey; width: 20px; background-color: '
    + br1
    + '; border-radius: 5px; } '
    'QComboBox QAbstractItemView { color: black; background-color: ' + br1 + '; } '
    'QComboBox QAbstractItemView::item:hover { color: black; background-color: '
    + br2
    + '; } '

    'QSpinBox { color: black; background-color: '
    + br1
    + '; selection-background-color: '
    + br3
    + '; selection-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; border: 1px solid grey; border-radius: 5px; } '
    'QSpinBox::up-button { border-left: 1px solid grey; width: 20px; background-color: '
    + br21
    + '; border-radius: 2px; } '
    'QSpinBox::up-button:hover { border-left: 1px solid grey; width: 20px; background-color: '
    + br1
    + '; border-radius: 2px; } '
    'QSpinBox::down-button { border-left: 1px solid grey; width: 20px; background-color: '
    + br2
    + '; border-radius: 2px; } '
    'QSpinBox::down-button:hover { border-left: 1px solid grey; width: 20px; background-color: '
    + br1
    + '; border-radius: 2px; } '

    'QDoubleSpinBox {color: black; background-color: '
    + br1
    + '; selection-background-color: '
    + br3
    + '; selection-color: '
    + br1
    + '; font-family: "Times New Roman"; font-size: 16px; border: 1px solid grey; border-radius: 5px; } '
    'QDoubleSpinBox::up-button { border-left: 1px solid grey; width: 20px; background-color: '
    + br21
    + '; border-radius: 2px; } '
    'QDoubleSpinBox::up-button:hover { border-left: 1px solid grey; width: 20px; background-color: '
    + br1
    + '; border-radius: 2px; } '
    'QDoubleSpinBox::down-button { border-left: 1px solid grey; width: 20px; background-color: '
    + br2
    + '; border-radius: 2px; } '
    'QDoubleSpinBox::down-button:hover { border-left: 1px solid grey; width: 20px; background-color: '
    + br1
    + '; border-radius: 2px; } '

    'QPushButton { border: 1px solid grey; border-radius: 5px; color: black; background-color: '
    + br2
    + '; font-family: "Times New Roman"; font-size: 16px; font-weight: bold; } '
    'QPushButton::hover { background-color: ' + br1 + '; } '
    'QPushButton::pressed { background-color: ' + br3 + '; color: ' + br1 + '; } '
    'QPushButton::checked { background-color: ' + br4 + '; color: ' + br1 + '; } '
)

def styler(inp):
    inp.setStyleSheet(st)
