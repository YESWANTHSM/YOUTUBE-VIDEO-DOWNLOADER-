import threading
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import yt_dlp
import os

def download_video():
    url = simpledialog.askstring("Video URL", "Enter the YouTube video URL:")
    if not url:
        return

    quality = simpledialog.askstring("Quality", "Enter the quality (e.g. 720p, 480p, best):")
    folder = filedialog.askdirectory(title="Choose download folder")
    if not folder:
        return

    options = {
        'format': f'bestvideo[height<={quality}]+bestaudio/best' if quality.isdigit() else quality,
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }

    def run_download():
        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            root.after(0, lambda: messagebox.showinfo("Success", "✅ Download completed!"))
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", f"❌ {str(e)}"))

    threading.Thread(target=run_download).start()

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("300x100")
root.resizable(False, False)

btn = tk.Button(root, text="Download Video", command=download_video)
btn.pack(pady=30)

root.mainloop()
