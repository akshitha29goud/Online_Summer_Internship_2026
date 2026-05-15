# WT2 - Image Preprocessing

## Objective
Resized images to lower dimensions while preserving aspect ratio.

## Work Done
- Used FFmpeg for resizing
- Maintained aspect ratio using 384:-1
- Preserved normalized YOLO labels

## Tools Used
- FFmpeg

## Command
ffmpeg -i input.jpg -vf scale=384:-1 output.jpg
