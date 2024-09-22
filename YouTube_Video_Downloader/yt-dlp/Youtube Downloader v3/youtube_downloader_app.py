import os
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# Function to download video/audio using yt-dlp with selected format and quality
def download_video():
    link = entry.get()

    if not link:
        messagebox.showerror("Error", "Please enter a valid YouTube link.")
        return

    # Get selected format and quality
    selected_format = format_var.get()
    selected_quality = quality_var.get()

    # Set quality options based on user selection
    quality_map = {
        '8K': 'bestvideo[height<=4320]+bestaudio/best[height<=4320]',
        '4K': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
        '2K': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
        'High': 'best',
        'Medium': 'best[height<=720]',
        'Low': 'worst'
    }
    quality_opt = quality_map[selected_quality]

    try:
        # Set download path to desktop
        download_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Use yt-dlp to download the video or audio with selected options
        if selected_format == "Video":
            command = f'yt-dlp -f "{quality_opt}" -o "{download_path}/%(title)s.%(ext)s" {link}'
        else:  # Audio format selected
            command = f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 -o "{download_path}/%(title)s.%(ext)s" {link}'

        subprocess.run(command, shell=True)

        messagebox.showinfo("Success", f"Download completed! Files saved to: {download_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {str(e)}")

# Function to exit the app
def exit_app():
    root.quit()

# Create the GUI
root = tk.Tk()
root.title("YouTube Downloader")

# Set the style for Windows 11 look
style = ttk.Style()
style.theme_use('clam')  # Use a clam theme for better appearance
style.configure('TButton', padding=6, relief="flat", background="#0078D4", foreground="white")
style.configure('TLabel', background="white", font=("Segoe UI", 12))
style.configure('TEntry', font=("Segoe UI", 12))

# Label for the link input
label = tk.Label(root, text="Paste YouTube Link Here:")
label.pack(pady=10)

# Entry for the link
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

# Set window size and display the GUI
root.geometry("400x300")
root.configure(bg="white")
root.mainloop()
