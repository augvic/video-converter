## 📽️ Video Converter

📼 A CLI tool for video format conversion.

## About

This tool converts video files to different formats using FFmpeg.

To use it, you must download FFmpeg and place the `ffmpeg.exe` file inside the `storage` folder located in the project root directory.

You provide:
- An input video file path.
- The desired output format.

The tool uses FFmpeg to perform the conversion.

After the conversion is completed, the output video will be available in the `storage/videos` folder.

Any unknown errors that occur during execution are logged in the `storage/logs` directory.

## Tech Stack

Languages:
- 🐍 Python.

External tools:
- 🎞️ FFmpeg.
