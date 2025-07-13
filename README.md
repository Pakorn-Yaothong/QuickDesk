# 🚀 QuickDesk – Smart Window Workspace Launcher

QuickDesk is a Python-based GUI utility that launches your favorite productivity tools (VSCode, Chrome, Discord) and arranges their window positions across one or two monitors automatically.

---

## 📦 Features

- One-click launch of:
  - VSCode with your selected project folder
  - Google Chrome with custom tab set
  - Discord
- Automatic window positioning using pixel coordinates
- Supports:
  - **Mode 1**: Single Display (VSCode + Chrome)
  - **Mode 2.1**: VSCode on Main, Chrome + Discord on Second Display
  - **Mode 2.2**: Chrome + VSCode on Main, Discord on Second Display

---

## 📁 Folder Structure

```
QuickDesk/
├── quickdesk_main.py
├── quickdesk_mode1.py
├── quickdesk_mode2.py
├── utils/
│   ├── app_launcher.py
│   └── window_manager.py
├── assets/
│   └── quickdesk_icon.ico
├── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pakorn-Yaothong/QuickDesk.git
cd QuickDesk
```

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install pywin32
```

#### `requirements.txt` includes:

```
pyqt5
pygetwindow
pyautogui
screeninfo
```

---

## ▶️ How to Run

```bash
python quickdesk_main.py
```

- Select a folder for VSCode
- Choose a mode
- Click **Launch QuickDesk**

---

## ⚠️ Requirements

- OS: **Windows only**
- Pre-installed applications (fixed paths, editable in `utils/app_launcher.py`):
  - **VSCode**  
    `C:\Users\<YourUsername>\AppData\Local\Programs\Microsoft VS Code\Code.exe`
  - **Chrome**  
    `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - **Discord**  
    Standard install via `%LOCALAPPDATA%\Discord\Update.exe`

---

## 🏗 Build as Windows Executable (.exe)

To package QuickDesk as a standalone Windows program:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build the `.exe`

```bash
pyinstaller --noconfirm --windowed --icon=assets/quickdesk_icon.ico quickdesk_main.py
```

> Output: `dist/quickdesk_main/quickdesk_main.exe`

### 3. Finalize for Distribution

- Copy the `assets/` folder into `dist/quickdesk_main/`
- Zip the folder or share as-is

✅ Users can now run `quickdesk_main.exe` without needing Python installed.

---

## 👨‍💻 Developer

**Pakorn Yaothong**  
Computer Engineering Student – Prince of Songkla University  
GitHub: [@Pakorn-Yaothong](https://github.com/Pakorn-Yaothong)

---

## 📄 License

TeamDev PSU  
Copyright (c) 2025  
**Pakorn Yaothong**
