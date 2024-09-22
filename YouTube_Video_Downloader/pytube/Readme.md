# Note [22-09-2024]: 
**Youtube API has been changed and PyTube is not working for video download. Please check new downloader using [yt-dlp](https://github.com/MustafaHelwa/MyTools/tree/main/YouTube_Video_Downloader/yt-dlp).**


# **YouTube Video and Audio Downloader (PyTube)**

## **Description**
This repository contains a Python script that allows users to download YouTube videos and audio files using the PyTube library. The script supports downloading videos in various quality options (including 2K, 4K, and 8K) and audio tracks in different bitrates. Users can download videos with or without audio, merge video and audio files, and customize download options through an intuitive interface.

## **Features**
- **Video Downloading**: Supports video downloads in multiple resolutions, including 2K, 4K, and 8K.
- **Audio Downloading**: Option to download audio-only files with adjustable quality settings.
- **Video & Audio Merge**: Merge video and audio tracks or download them separately.
- **Progress Tracking**: Displays download progress as a percentage.
- **Custom Quality Options**: Choose from a variety of video and audio quality settings.
- **User-friendly Interface**: Simple and professional interface that matches the Windows 11 theme.

## **How to Use**

### **Manual Download**
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies:
    ```bash
    pip install pytube
    ```
4. Navigate to the directory containing the script.
5. Run the script using Python:
    ```bash
    python youtube_downloader.py
    ```
6. Follow the on-screen instructions to input the YouTube video URL and choose download options.

### **Automatic Download**
1. Clone or download this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies:
    ```bash
    pip install pytube
    ```
4. Run the script and specify your preferred download settings (video/audio quality, format, etc.).

## **Simple Code Example** 
Here's a basic example of how to use PyTube to download YouTube videos:
```
#Use Your CMD
#Go to your file directory (such as desktop)

#for High quality Video download:
pytube [URL] -v

#for Audio download:
pytube [URL] -a
```

## **Detailed Code Example**
Here's some detailed example of how to use PyTube to download YouTube videos:

```python
from pytube import YouTube

# Function to show progress during download
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Download progress: {int(percentage)}%")

# Enter the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create YouTube object
yt = YouTube(video_url, on_progress_callback=on_progress)

# Select the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Download the video
print("Downloading video...")
video_stream.download(output_path=".", filename="downloaded_video.mp4")
print("Download complete!")
```

## Dependencies: 
- Python 3.x
- PyTube library (Install using pip install pytube)
- FFmpeg for merging video and audio files (Ensure FFmpeg is installed and added to your system path)

## File Structure: 
- youtube_downloader.py: Main Python script for downloading YouTube videos and audio.
- README.md: Readme file providing information about the script and usage instructions.

## Troubleshooting:
- FFmpeg Not Found: Ensure FFmpeg is installed and the path is added to your system’s environment variables.
- Download Issues: If downloads fail, make sure the video URL is correct and supported by PyTube.

## Credits:
- This script is built using the PyTube library for YouTube video downloads.
- Developed by Mustafa Helwa.
