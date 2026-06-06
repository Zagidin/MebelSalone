import sys
import os
from UI.login import LoginDialog
from database.init_db import create_tables
from UI.products import ProductsWindow
from PyQt6.QtWidgets import QApplication
from configs.config_import import main_import_data
from PyQt6.QtGui import QFont, QIcon
from configs.config_ui import APP_ICON_ICO, APP_ICON_PNG
from configs.path_utils import get_app_dir


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Calibri", 10))

    if os.path.exists(APP_ICON_ICO):
        app.setWindowIcon(QIcon(APP_ICON_ICO))
    elif os.path.exists(APP_ICON_PNG):
        app.setWindowIcon(QIcon(APP_ICON_PNG))

    login = LoginDialog()
    if not login.exec():
        sys.exit(0)

    window = ProductsWindow(login.user_data)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    db_path = os.path.join(get_app_dir(), "MebelSalone.db")
    create_tables()
    main_import_data()
    main()