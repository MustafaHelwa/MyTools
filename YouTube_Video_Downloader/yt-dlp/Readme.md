
# **YouTube Video and Audio Downloader (yt-dlp)**

## **Description**
This repository contains a Python script that allows users to download YouTube videos and audio files using the `yt-dlp` library. The script features a graphical user interface (GUI) built with `Tkinter` for selecting video/audio formats and choosing from a range of quality options (8K, 4K, 2K, etc.). The downloaded files are saved directly to the user's desktop.

## **Features**
- **Video Downloading**: Supports downloading YouTube videos in multiple resolutions including 8K, 4K, and 2K.
- **Audio Downloading**: Allows downloading audio-only files in MP3 format.
- **Custom Quality Options**: Users can select from quality options ranging from 8K to Low (worst).
- **GUI Interface**: Provides an easy-to-use graphical user interface for selecting formats and quality.
- **Progress Notification**: Notifies the user when the download is complete or if an error occurs.

## **How to Use**

### **Step-by-Step Guide**
1. **Clone or Download the Repository**:
   Download this repository to your local machine.

2. **Install Python**:
   Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

3. **Install Dependencies**:
   Install the required libraries:
   ```
   pip install yt-dlp tkinter
   ```
   Then install modified FFmpeg
   ```
   winget install "FFmpeg (Essentials Build)"
   ```
   
5. **Run the Script**:
 Navigate to the directory where the script is located and run it using Python:

    ```
    python youtube_downloader_gui.py
    ```

6. **Using the GUI**:

- Paste the YouTube video link in the input field.
- Select whether you want to download Video or Audio from the dropdown menu.
- Choose the preferred quality (8K, 4K, 2K, High, Medium, or Low).
- Click the "Download" button to start the download.
- The downloaded file will be saved to your desktop.

# Simple Code Example
  Here is a simple code example for downloading a YouTube video using the yt-dlp library via command-line:

  ```Python
# Download video in best quality
yt-dlp -f best [URL]

# Download audio in MP3 format
yt-dlp -f bestaudio --extract-audio --audio-format mp3 [URL]

# Download best Video/Audio file available (please refer to `FFmpeg` below)
yt-dlp -f bestvideo+bestaudio [URL]
```

# Detailed Code Explanation
Here’s a detailed explanation of how the GUI-based YouTube downloader script works:
```Python
import os
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# Function to download video/audio using yt-dlp with selected format and quality
def download_video():
    link = entry.get()  # Get the YouTube link from the user input

    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube link.")  # Error handling for missing input
        return

    # Get selected format (Video/Audio) and quality from the dropdown menus
    selected_format = format_var.get()
    selected_quality = quality_var.get()

    # Map user-selected quality to yt-dlp format codes
    quality_map = {
        '8K': 'bestvideo[height<=4320]+bestaudio/best[height<=4320]',
        '4K': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
        '2K': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
        'High': 'best',
        'Medium': 'best[height<=720]',
        'Low': 'worst'
    }
    quality_opt = quality_map[selected_quality]  # Choose the correct quality option

    try:
        # Set the download path to the user's desktop
        download_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Build the yt-dlp command for video or audio download
        if selected_format == "Video":
            command = f'yt-dlp -f "{quality_opt}" -o "{download_path}/%(title)s.%(ext)s" {link}'
        else:  # For audio download
            command = f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 -o "{download_path}/%(title)s.%(ext)s" {link}'

        # Run the yt-dlp command
        subprocess.run(command, shell=True)

        # Notify the user when download completes
        messagebox.showinfo("Success", f"Download completed! Files saved to: {download_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {str(e)}")  # Error handling for download failure

# Function to exit the app
def exit_app():
    root.quit()

# Create the GUI interface using Tkinter
root = tk.Tk()
root.title("YouTube Downloader")

# Set the style for Windows 11 look
style = ttk.Style()
style.theme_use('clam')  # Use the 'clam' theme for modern appearance
style.configure('TButton', padding=6, relief="flat", background="#0078D4", foreground="white")
style.configure('TLabel', background="white", font=("Segoe UI", 12))
style.configure('TEntry', font=("Segoe UI", 12))

# Label for the YouTube link input
label = tk.Label(root, text="Paste YouTube Link Here:")
label.pack(pady=10)

# Entry field for the YouTube link
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Dropdown menu for selecting format (Video/Audio)
format_label = tk.Label(root, text="Select Format:")
format_label.pack(pady=5)
format_var = tk.StringVar()
format_menu = ttk.Combobox(root, textvariable=format_var, values=["Video", "Audio"], state="readonly")
format_menu.pack(pady=5)
format_menu.current(0)  # Default to "Video"

# Dropdown menu for selecting quality
quality_label = tk.Label(root, text="Select Quality:")
quality_label.pack(pady=5)
quality_var = tk.StringVar()
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=["8K", "4K", "2K", "High", "Medium", "Low"], state="readonly")
quality_menu.pack(pady=5)
quality_menu.current(0)  # Default to "High"

# Download button
download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Set window size and configure background
root.geometry("400x300")
root.configure(bg="white")
root.mainloop()
```

## Make your Downloader.EXE

```bash
pyinstaller --onefile --noconsole youtube_downloader_app.py
```

## Key Points:
- The yt-dlp library is used for downloading both video and audio from YouTube.
- The script allows users to select their preferred format (Video or Audio) and quality (8K to Low).
- Downloads are automatically saved to the user's desktop.
- The GUI is built using Tkinter to make the tool user-friendly.

## Dependencies
- Python 3.7+
- yt-dlp library (Install using `pip install yt-dlp`)
- Modified FFmpeg requires Windows 7 or later (Install using `winget install "FFmpeg (Essentials Build)"`)
- Tkinter for creating the GUI (comes pre-installed with Python)

## Troubleshooting
- Download Issues: Ensure the YouTube link is correct and valid.
- FFmpeg Not Found: If FFmpeg is required for audio extraction or merging, ensure it's installed and added to your system’s environment variables.

```bash
# Best way to download edited ffmpeg (not python original):
winget install "FFmpeg (Essentials Build)"  
```

## Credits
- This script is built using the yt-dlp library for YouTube video and audio downloads.
- For more info, please check [FFmpeg](https://github.com/yt-dlp/FFmpeg-Builds) & [yt-dlp](https://github.com/yt-dlp/yt-dlp) libraries. 
- Developed by Mostafa Helwa.
