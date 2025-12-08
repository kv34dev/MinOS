from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
import os

class OpenNote(QWidget):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

        layout = QVBoxLayout()
        self.field = QTextEdit()

        # Загружаем файл
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                self.field.setText(f.read())

        # Автосохранение заметки
        self.field.textChanged.connect(self.save_note)

        layout.addWidget(self.field)
        self.setLayout(layout)

    def save_note(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(self.field.toPlainText())
