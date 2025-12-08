from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class Notes(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.field = QTextEdit()

        # Чистый файл — ничего не загружаем
        self.field.setPlaceholderText("Введите текст заметки...")

        layout.addWidget(self.field)
        self.setLayout(layout)
