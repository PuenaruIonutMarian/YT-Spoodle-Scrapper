# YT-Spoodle-Scrapper

## 📌 Description
YT-Spoodle-Scrapper is a simple Python-based YouTube playlist downloader that extracts audio from videos and converts them into high-quality MP3 files. It utilizes `yt-dlp` for downloading and `ffmpeg` for audio processing.

## 🚀 Features
- Download entire YouTube playlists as MP3 files
- Automatically extracts and converts audio
- Saves files in a structured `downloads/` folder
- Supports high-quality 192kbps audio conversion

## 📂 Installation

### 1️⃣ Prerequisites
Ensure you have Python installed (3.7+ recommended). If you don’t have it, download it from [Python.org](https://www.python.org/downloads/).

### 2️⃣ Install Required Packages
Open a terminal or command prompt and run:
```sh
pip install yt-dlp
pip install ffmpeg
```

If `ffmpeg` is not installed on your system, install it via Chocolatey:
```sh
choco install ffmpeg
```

### 3️⃣ Clone or Download the Repository
```sh
git clone https://github.com/PuenaruIonutMarian/YT-Spoodle-Scrapper.git
cd YT-Spoodle-Scrapper
```

## 🎯 Usage
Run the script in a terminal:
```sh
python main.py
```
Then, enter the YouTube playlist URL when prompted. The downloaded files will be saved in the `downloads/` folder.

## 🔧 Convert to .exe (Windows Only)
To create a standalone executable, install `pyinstaller`:
```sh
pip install pyinstaller
```
Then, generate the `.exe` file:
```sh
pyinstaller --onefile --noconsole main.py
```
The `.exe` file will be created inside the `dist/` folder.

## 📜 License
This project is licensed under the MIT License.

## 💡 Contributing
Pull requests and feature suggestions are welcome! Open an issue or fork the repo to get started.

## 📞 Support
If you encounter any issues, feel free to create an issue in the repository or contact me directly.

---

Enjoy downloading your favorite YouTube playlists hassle-free with **YT-Spoodle-Scrapper**! 🎵🔥

