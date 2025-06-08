from PyQt6.QtWidgets import QApplication
import sys
from ui.login_form import LoginForm  # импорт формы

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LoginForm()
    form.show()
    sys.exit(app.exec())
