import os
import tkinter as tk
from tkinter import filedialog, Toplevel
import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image, ImageTk
import io

class MusicPlayer:
    def __init__(self):
        self.folder_path = self.choose_folder()
        self.playlist = self.load_music_files()
        self.current_index = 0
        pygame.mixer.init()
        self.album_art_window = None

        if self.playlist:
            print("\n🎵 Music files found:\n")
            self.display_playlist()
        else:
            print("No MP3 files found in the selected folder.")

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

    def play(self, index):
        if 0 <= index < len(self.playlist):
            pygame.mixer.music.load(self.playlist[index])
            pygame.mixer.music.play()
            self.current_index = index
            _, _, _, album_art = self.extract_metadata(self.playlist[index])
            self.display_album_art(album_art)

    def display_album_art(self, image):
        if self.album_art_window:
            self.album_art_window.destroy()

        if image:
            self.album_art_window = Toplevel()
            self.album_art_window.title("Album Art")
            img = ImageTk.PhotoImage(image)
            label = tk.Label(self.album_art_window, image=img)
            label.image = img
            label.pack()

if __name__ == "__main__":
    player = MusicPlayer()
    player.play(0)  # Example to play first track
