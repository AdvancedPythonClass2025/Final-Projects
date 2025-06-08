import os
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self):
        self.folder_path = self.choose_folder()
        self.playlist = self.load_music_files()

    def choose_folder(self):
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory(title="Select Music Folder")
        return folder_selected if folder_selected else ""

    def load_music_files(self):
        return [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith(".mp3")] if self.folder_path else []

if __name__ == "__main__":
    player = MusicPlayer()
    print("Music files found:", player.playlist)
