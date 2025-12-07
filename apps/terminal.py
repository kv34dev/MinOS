from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
import os


class Terminal(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.input = QLineEdit()

        self.input.returnPressed.connect(self.run_command)

        layout.addWidget(self.output)
        layout.addWidget(self.input)
        self.setLayout(layout)

        self.print_line("MinOS Terminal v1.0")
        self.print_line("Type 'help' to see the list of commands.")

    def print_line(self, text):
        self.output.append(text)

    def run_command(self):
        cmd = self.input.text().strip()
        self.print_line(f"> {cmd}")

        if cmd == "":
            pass

        elif cmd == "help":
            self.print_line(
                "Available commands:\n"
                " help        - show list of commands\n"
                " echo TEXT   - print text\n"
                " clear       - clear the screen\n"
                " about       - system information\n"
                " ls          - list files\n"
                " cat FILE    - show file contents\n"
                " touch FILE  - create file\n"
            )

        elif cmd.startswith("echo "):
            self.print_line(cmd[5:])

        elif cmd == "clear":
            self.output.clear()

        elif cmd == "about":
            self.print_line("MinOS — an OS running inside a Python window. ")

        elif cmd == "ls":
            files = os.listdir(".")
            if not files:
                self.print_line("(empty)")
            else:
                for f in files:
                    self.print_line(f)

        elif cmd.startswith("cat "):
            filename = cmd[4:].strip()
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    self.print_line(f.read())
            else:
                self.print_line("File not found.")

        elif cmd.startswith("touch "):
            filename = cmd[6:].strip()
            with open(filename, "w", encoding="utf-8") as f:
                pass
            self.print_line(f"File '{filename}' created.")

        else:
            self.print_line("Unknown command. Type 'help'.")

        self.input.clear()
