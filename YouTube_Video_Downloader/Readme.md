# YouTube Video and Audio Downloader
## Description:
This folder contains a Python script for downloading YouTube videos and audio files using the yt-dlp library. Initially, I relied on the `PyTube` library for over a year to perform video downloads, but a major YouTube API update impacted its functionality. To ensure continued support for high-quality video and audio downloads, I transitioned to the more powerful `yt-dlp` library. The script provides a user-friendly interface, allowing users to download videos in various resolutions, extract audio files, and choose between different quality options.

## Features:
- Video Downloading: Download YouTube videos in various resolutions, including 8K, 4K, 2K, High, Medium, and Low quality.
- Audio Downloading: Extract and download audio tracks only in MP3 format, ideal for music, podcasts, or audio-focused content.
- Custom Quality Options: Allows users to select from multiple video and audio quality settings based on their preferences or device storage limitations.
- Progress Notification: Provides real-time notifications for download progress and completion. Notifies the user in case of any errors.
- Automatic File Saving: All downloaded files are automatically saved to the desktop for easy access.
- User-Friendly GUI: An intuitive graphical user interface (GUI) makes it easy to use for anyone, even without command-line experience.

## How to Use the Downloader:
- Clone or download this repository to your local machine.
- Ensure you have Python installed.
- Install the required libraries using:
    ```
    pip install yt-dlp tkinter
    winget install "FFmpeg (Essentials Build)"
    ```
    - Navigate to the directory containing the script.
    - Run the script using Python:
    For top quality: 
    ```
    # Move to your desired dowload folder using CMD
    yt-dlp -f bestvideo+bestaudio [YT URL]
    ```
    For all audio/video quality options: 
    
    ```
    yt-dlp --list-formats [YT URL]
    ```
    then Choose your desired Format number (in green) 
    ![Result prompt](https://github.com/user-attachments/assets/fb6c3c71-09b7-4d83-ad2f-b69a29fdcfa1)
    
    The files will be automatically saved to your desktop.

## Dependencies:
- Python 3.x: The script requires Python 3.x to run. If Python is not installed, download it from [here](https://www.python.org/downloads/).
- yt-dlp: A powerful command-line program used to download videos from YouTube and many other websites. Install using:
    ```
    pip install yt-dlp
    ```
- Tkinter: A standard Python library for creating graphical user interfaces (GUI). It comes pre-installed with Python, but you can install it manually if needed using:
    ```
    pip install tkinter
    ```
- FFmpeg: a Modified Python library for combining audio and video files. Install using:
    ```
    winget install "FFmpeg (Essentials Build)"
    ```

## File Structure:
- youtube_downloader_gui.py: The main Python script for downloading YouTube videos and audio files.
- youtube_downloader_app.exe: The main GUI tool for video download.
- README.md: This readme file providing an overview of the script and instructions for usage.

## Credits:
- Mustafa Helwa: Developer of the current Python script utilizing yt-dlp and Tkinter to provide an easy-to-use YouTube downloader.
- yt-dlp: Developed by a community of contributors, yt-dlp is an enhanced version of youtube-dl that supports additional features and website integrations.
- PyTube: Initially used for this project, PyTube was a powerful library until a YouTube API update affected its functionality.

By combining the functionality of yt-dlp and the ease of use provided by Tkinter, this downloader offers a comprehensive solution for downloading YouTube content in high quality, with minimal effort required from the user.
