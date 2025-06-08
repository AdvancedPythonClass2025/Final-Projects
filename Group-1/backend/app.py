import os
import tkinter as tk
from tkinter import filedialog
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
import io

class MusicPlayer:
    def __init__(self):
        self.folder_path = self.choose_folder()
        self.playlist = self.load_music_files()
        self.display_playlist()

    def choose_folder(self):
        root = tk.Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory(title="Select Music Folder")
        return folder_selected if folder_selected else ""

    def load_music_files(self):
        return [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.endswith(".mp3")] if self.folder_path else []

    def extract_metadata(self, file):
        audio = MP3(file, ID3=ID3)
        title = audio.get("TIT2").text[0] if audio.get("TIT2") else "Unknown Title"
        artist = audio.get("TPE1").text[0] if audio.get("TPE1") else "Unknown Artist"
        duration = audio.info.length if audio.info else 0
        album_art = self.extract_album_art(audio)
        return title, artist, duration, album_art

    def extract_album_art(self, audio):
        if "APIC:" in audio.tags:
            image_data = audio.tags["APIC:"].data
            return Image.open(io.BytesIO(image_data))
        return None

    def display_playlist(self):
        for i, file in enumerate(self.playlist):
            title, artist, duration, album_art = self.extract_metadata(file)
            print(f"{i+1}. {title} - {artist} ({duration:.2f} sec)")
            if album_art:
                album_art.show()

if __name__ == "__main__":
    player = MusicPlayer()
