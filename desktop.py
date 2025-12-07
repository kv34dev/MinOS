from PySide6.QtWidgets import QWidget, QPushButton
from window import AppWindow
from apps.terminal import Terminal
from apps.notes import Notes

class Desktop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MinOS")
        self.resize(800, 600)

        self.windows = []

        btn_terminal = QPushButton("Terminal", self)
        btn_terminal.move(20, 20)
        btn_terminal.clicked.connect(self.open_terminal)

        btn_notes = QPushButton("Notes", self)
        btn_notes.move(20, 60)
        btn_notes.clicked.connect(self.open_notes)

    def open_terminal(self):
        win = AppWindow("Terminal", Terminal())
        self.windows.append(win)
        win.show()

    def open_notes(self):
        win = AppWindow("Notes", Notes())
        self.windows.append(win)
        win.show()
