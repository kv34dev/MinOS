from PySide6.QtWidgets import QMainWindow

class AppWindow(QMainWindow):
    def __init__(self, title, widget):
        super().__init__()
        self.setWindowTitle(title)
        self.setCentralWidget(widget)
        self.resize(400, 300)
