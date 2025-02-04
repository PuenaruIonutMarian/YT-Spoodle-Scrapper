import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_playlist():
    playlist_url = url_entry.get()
    if not playlist_url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

# Interface Graphique
root = tk.Tk()
root.title("YouTube Playlist Downloader")

tk.Label(root, text="Enter YouTube Playlist URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_playlist)
download_button.pack()

root.mainloop()
