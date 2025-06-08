from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon
import sys, os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))



class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()

        registr_path = os.path.join(BASE_DIR, "resources", "icons", "registr.png")

        self.setWindowTitle("Регистрация")
        self.setWindowIcon(QIcon(registr_path))

        self.last_name_label = QLabel("Фамилия:")
        self.last_name_input = QLineEdit()

        self.first_name_label = QLabel("Имя:")
        self.first_name_input = QLineEdit()

        self.middle_name_label = QLabel("Отчество:")
        self.middle_name_input = QLineEdit()

        self.phone_label = QLabel("Телефон:")
        self.phone_input = QLineEdit()

        self.address_label = QLabel("Адрес:")
        self.address_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_password_label = QLabel("Повторите пароль:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_button = QPushButton("Зарегистрироваться")

        layout = QVBoxLayout()
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)

        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)

        layout.addWidget(self.middle_name_label)
        layout.addWidget(self.middle_name_input)

        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)

        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def handle_register(self):
        password = self.password_input.text()
        confirm = self.confirm_password_input.text()

        if password != confirm:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают!")
            return

        QMessageBox.information(self, "Успешно", "Регистрация прошла успешно.")

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        login_path = os.path.join(BASE_DIR, "resources", "icons", "login.png")

        self.setWindowTitle("Вход в систему")
        self.setWindowIcon(QIcon(login_path))
        self.resize(300, 150)

        # Создаем виджеты
        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # Скрыть пароль

        self.login_button = QPushButton("Войти")
        self.register_button = QPushButton("Регистрация")

        # Размещаем виджеты вертикально
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.handle_login)
        self.register_button.clicked.connect(self.open_register_form)

    def handle_login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if login == "admin" and password == "123":
            print("Успешный вход")
        else:
            print("Неверный логин или пароль")

    def open_register_form(self):
        self.register_window = RegisterForm()
        self.register_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создаем приложение
    window = LoginForm()          # Создаем окно логина
    window.show()                 # Показываем окно
    sys.exit(app.exec())          # Запускаем цикл обработки событий
