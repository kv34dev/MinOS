from PySide6.QtWidgets import QApplication
from desktop import Desktop
import sys

def main():
    app = QApplication(sys.argv)
    desktop = Desktop()
    desktop.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
