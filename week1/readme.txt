Week 01 - FFmpeg Tasks
Task 1: Video to Frames
Extracted multiple images from a video using FFmpeg.
### Command:
ffmpeg -i playbackvideo.mp4 -r 1 image-%03d.jpg

Task 2: Frames to Video
Generated 1800 frames (30 fps × 60 seconds) and converted them back to a 1-minute video.
### Commands:
Extract frames:
ffmpeg -ss 00:00:00 -t 60 -i playbackvideo.mp4 -r 30 frame-%04d.jpg
Convert to video:
ffmpeg -framerate 30 -i frame-%04d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4

Task 3: Add Audio to Video
Merged a 1-minute audio track with the generated video.
### Commands:
Trim audio:
ffmpeg -i audio.mp3 -t 60 audio_1min.mp3
Merge audio + video:
ffmpeg -i output.mp4 -i audio_1min.mp3 -c:v copy -c:a aac -shortest final_video.mp4

Final Output Video
https://drive.google.com/file/d/1nwQwiJGbo0j6so7AMSOennJgMGnKCeRr/view?usp=sharing

 Audio Source
https://drive.google.com/file/d/1EmL_nGPQb_ICdGXSMRhmTMuoy0XwzBa6/view?usp=sharing

Video Source
https://youtu.be/ryUxrFUk6MY?si=xYfFlwEiybhDj4MZhttps://youtu.be/ryUxrFUk6MY?si=xYfFlwEiybhDj4MZhttps://youtu.be/ryUxrFUk6MY?si=xYfFlwEiybhDj4MZ
