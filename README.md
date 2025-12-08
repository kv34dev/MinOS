# MinOS — A Mini Operating System Inside a Window  
A fully custom “virtual operating system” built entirely in Python using PySide6.  
PythonOS simulates a desktop environment with apps, files, a terminal, and more — all running inside a single window on macOS, Windows, or Linux.

## Features

### Desktop Environment
- Custom desktop window  
- Desktop icons (e.g., `note1.txt`)  
- Launchable apps  
- Multiple windows with persistent references  

### Notes System
- **New Note App** — always opens with a clean blank document  
- **Desktop Note Files** — stored inside `desktop_files/`  
- Automatic saving when editing  
- Separate viewer/editor for existing notes  

### Terminal App
Includes built-in commands:
```
help         - list all commands
echo TEXT    - print text
clear        - clear the screen
about        - system information
ls           - list files
cat FILE     - show file content
touch FILE   - create new file
```

### Easily Extensible
The project is simple to expand:
- Add more apps  
- Add a file manager  
- Add icons and a dock  
- Add window dragging, animations, themes, etc.  

## Project Structure
```
MinOS/
│
├── main.py
├── desktop.py
├── window.py
├── desktop_files/
│   └── note1.txt
└── apps/
    ├── notes.py        # App for creating new blank notes
    ├── open_note.py    # App for editing existing note files
    └── terminal.py     # Terminal emulator with built-in commands
```

## Installation & Running

1. Install dependencies
```
pip install PySide6
```
2. Run the OS
```
python3 main.py
```
The OS will open in a standalone window.

## License

MIT License — free to use, modify, and distribute.
