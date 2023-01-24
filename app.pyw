from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QMessageBox
from create_passwordui import Ui_Form as CreatePasswordUI
from customtypes import CharacterTypes
from password_controller import PasswordController
import pyperclip



class CreatePasswordWidget(QWidget, CreatePasswordUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.allowed_characters: CharacterTypes = {'uppercase': False, 'lowercase': False, 'digits': False, 'symbols': False}
        self.length: int = 0
        self.uppercase_check.clicked.connect(self.uppercase_check_handler)
        self.lowercase_check.clicked.connect(self.lowercase_check_handler)
        self.digits_check.clicked.connect(self.digits_check_handler)
        self.symbols_check.clicked.connect(self.symbols_check_handler)
        self.length_input.textChanged.connect(self.length_input_handler)
        self.prepare_button.clicked.connect(self.prepare_chandler)
        self.copy_button.clicked.connect(self.copy_handler)
        
    def uppercase_check_handler(self, checked: bool) -> None:
        self.allowed_characters['uppercase'] = checked
    def lowercase_check_handler(self, checked: bool) -> None:
        self.allowed_characters['lowercase'] = checked
    def digits_check_handler(self, checked: bool) -> None:
        self.allowed_characters['digits'] = checked
    def symbols_check_handler(self, checked: bool) -> None:
        self.allowed_characters['symbols'] = checked
        
    def prepare_chandler(self):
        pc = PasswordController(self.length, self.allowed_characters)
        self.result = pc.get_random_password()
        self.result_label.setText(self.result)
        
    def copy_handler(self):
        pyperclip.copy(self.result)
        QMessageBox.information(self, 'Bildiris', 'Sifre Ugurla Kopyalandi!')
        
        
    def length_input_handler(self, value: str) -> None:
        self.length = int(value)
        


# Subclass QMainWindow to customize your application's main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Create App")
        # Set the central widget of the Window.
        create_password_widget = CreatePasswordWidget()
        self.setFixedSize(create_password_widget.size())
        self.setCentralWidget(create_password_widget)
        


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
