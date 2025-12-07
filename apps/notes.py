from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
import os

SAVE_FILE = "notes.txt"

class Notes(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.field = QTextEdit()

        # Загружаем заметки
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                self.field.setText(f.read())

        # Событие при изменении текста
        self.field.textChanged.connect(self.save_notes)

        layout.addWidget(self.field)
        self.setLayout(layout)

    def save_notes(self):
        text = self.field.toPlainText()
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write(text)
