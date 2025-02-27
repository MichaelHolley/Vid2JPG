# Vid2JPG Converter 🎥 → 🖼️

A simple desktop application built with Python and Tkinter that converts video files into sequences of JPG images.

## Features

- User-friendly graphical interface
- Progress bar visualization during conversion
- Automatic timestamped output folders
- Support for common video formats (.mp4, .avi, .wmv)

## Requirements ⚙️

This project uses `uv` for dependency management. Required packages:

- Python 3.x
- OpenCV (cv2)
- tkinter

## Usage 🚀

1. Click "Select" to choose your input video file
2. Click "Select" to choose your output folder
3. Click "Start" to begin the conversion

The application will create a new folder with the current timestamp (format: YYYYMMDD_HHMMSS) in your selected output directory and save all frames as sequential JPG images. For example: `20240215_143022`.

Each frame will be saved as `frame_XXXX.jpg` where XXXX is the sequential frame number.

## Supported Formats 📁

Currently supports the following video formats:

- .mp4
- .avi
- .wmv
