import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class VideoSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Splitter")
        self.create_widgets()

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

        self.split_btn = tk.Button(self.root, text="Split Video", command=self.split_video)
        self.split_btn.pack()

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        self.status_label.config(text=f"Selected Video: {self.video_path}")

    def split_video(self):
        start_time = int(self.start_entry.get())
        end_time = int(self.end_entry.get())
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video files", "*.mp4")])

        video = VideoFileClip(self.video_path)
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(output_path)
        self.status_label.config(text=f"Video saved to: {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSplitterApp(root)
    root.mainloop()
