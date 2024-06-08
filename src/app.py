import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import pygame

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.create_widgets()
        self.video = None

    def create_widgets(self):
        self.upload_btn = tk.Button(self.root, text="Upload Video", command=self.upload_video)
        self.upload_btn.pack()

        self.start_label = tk.Label(self.root, text="Start Time (in seconds):")
        self.start_label.pack()
        self.start_entry = tk.Entry(self.root)
        self.start_entry.pack()

        self.end_label = tk.Label(self.root, text="End Time (in seconds):")
        self.end_label.pack()
        self.end_entry = tk.Entry(self.root)
        self.end_entry.pack()

        self.play_btn = tk.Button(self.root, text="Play Segment", command=self.play_segment)
        self.play_btn.pack()

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        self.status_label.config(text=f"Selected Video: {self.video_path}")
        self.video = VideoFileClip(self.video_path)

    def play_segment(self):
        if self.video is None:
            self.status_label.config(text="Please upload a video first.")
            return

        try:
            start_time = int(self.start_entry.get())
            end_time = int(self.end_entry.get())

            if start_time >= end_time or start_time < 0 or end_time > self.video.duration:
                self.status_label.config(text="Invalid start or end time.")
                return

            clip = self.video.subclip(start_time, end_time)
            clip.preview()
        except ValueError:
            self.status_label.config(text="Please enter valid start and end times.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
