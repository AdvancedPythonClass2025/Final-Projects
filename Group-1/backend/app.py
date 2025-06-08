import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self):
        self.folder_path = self.choose_folder()

    def choose_folder(self):
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory(title="Select Music Folder")
        return folder_selected if folder_selected else ""

if __name__ == "__main__":
    player = MusicPlayer()
    print(f"Selected Folder: {player.folder_path}")

