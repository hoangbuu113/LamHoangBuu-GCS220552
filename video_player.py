import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
from tkinter import filedialog
import video_library as lib
from PIL import Image, ImageTk
import cv2
import pygame  # Import pygame for audio playback

class VideoPlayerGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Video Player")
        self.playlist = []
        self.video_source = ""
        self.vid = None
        self.pause = False

        pygame.mixer.init()  # Initialize the pygame mixer for audio playback

        # Create a tabbed interface
        self.tab_control = ttk.Notebook(window)

        self.check_videos_tab = ttk.Frame(self.tab_control)
        self.create_playlist_tab = ttk.Frame(self.tab_control)
        self.update_ratings_tab = ttk.Frame(self.tab_control)
        self.play_video_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.check_videos_tab, text="Check Videos")
        self.tab_control.add(self.create_playlist_tab, text="Create Playlist")
        self.tab_control.add(self.update_ratings_tab, text="Update Ratings")
        self.tab_control.add(self.play_video_tab, text="Play Video")

        self.tab_control.pack(expand=1, fill="both")

        # Initialize each tab
        self.init_check_videos_tab()
        self.init_create_playlist_tab()
        self.init_update_ratings_tab()
        self.init_play_video_tab()

    def init_check_videos_tab(self):
        list_videos_btn = tk.Button(self.check_videos_tab, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self.check_videos_tab, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt_check = tk.Entry(self.check_videos_tab, width=5)
        self.input_txt_check.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(self.check_videos_tab, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self.check_videos_tab, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(self.check_videos_tab, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl_check = tk.Label(self.check_videos_tab, text="", font=("Helvetica", 10))
        self.status_lbl_check.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.image_lbl = tk.Label(self.check_videos_tab)  # Label to display the video image
        self.image_lbl.grid(row=3, column=0, columnspan=4, pady=10)

        # Add Play and Stop buttons for MP3 playback
        play_audio_btn = tk.Button(self.check_videos_tab, text="Play Audio", command=self.play_audio)
        play_audio_btn.grid(row=4, column=0, padx=10, pady=10)

        stop_audio_btn = tk.Button(self.check_videos_tab, text="Stop Audio", command=self.stop_audio)
        stop_audio_btn.grid(row=4, column=1, padx=10, pady=10)

        self.list_videos_clicked()

    def init_create_playlist_tab(self):
        enter_lbl = tk.Label(self.create_playlist_tab, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt_playlist = tk.Entry(self.create_playlist_tab, width=5)
        self.input_txt_playlist.grid(row=0, column=1, padx=10, pady=10)

        add_video_btn = tk.Button(self.create_playlist_tab, text="Add to Playlist", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        search_lbl = tk.Label(self.create_playlist_tab, text="Search (by Name or Director)")
        search_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.search_txt = tk.Entry(self.create_playlist_tab, width=20)
        self.search_txt.grid(row=1, column=1, padx=10, pady=10)

        search_btn = tk.Button(self.create_playlist_tab, text="Search", command=self.search_videos_clicked)
        search_btn.grid(row=1, column=2, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(self.create_playlist_tab, width=50, height=15, wrap="none")
        self.playlist_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        play_btn = tk.Button(self.create_playlist_tab, text="Play Playlist", command=self.play_playlist_clicked)
        play_btn.grid(row=3, column=0, padx=10, pady=10)

        reset_btn = tk.Button(self.create_playlist_tab, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_btn.grid(row=3, column=1, padx=10, pady=10)

        self.status_lbl_playlist = tk.Label(self.create_playlist_tab, text="", font=("Helvetica", 10))
        self.status_lbl_playlist.grid(row=5, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    def init_update_ratings_tab(self):
        video_num_lbl = tk.Label(self.update_ratings_tab, text="Enter Video Number")
        video_num_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.video_num_txt = tk.Entry(self.update_ratings_tab, width=5)
        self.video_num_txt.grid(row=0, column=1, padx=10, pady=10)

        new_rating_lbl = tk.Label(self.update_ratings_tab, text="Enter New Rating")
        new_rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_txt = tk.Entry(self.update_ratings_tab, width=5)
        self.new_rating_txt.grid(row=1, column=1, padx=10, pady=10)

        update_rating_btn = tk.Button(self.update_ratings_tab, text="Update Rating", command=self.update_rating_clicked)
        update_rating_btn.grid(row=2, column=0, padx=10, pady=10)

        self.video_details_txt = tk.Text(self.update_ratings_tab, width=40, height=4, wrap="none")
        self.video_details_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl_update = tk.Label(self.update_ratings_tab, text="", font=("Helvetica", 10))
        self.status_lbl_update.grid(row=4, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def init_play_video_tab(self):
        self.canvas = tk.Canvas(self.play_video_tab, width=640, height=480)
        self.canvas.pack()

        open_video_btn = tk.Button(self.play_video_tab, text="Open Video", command=self.open_video)
        open_video_btn.pack(anchor=tk.CENTER, pady=10)

        play_video_btn = tk.Button(self.play_video_tab, text="Play", command=self.play_video)
        play_video_btn.pack(anchor=tk.CENTER, pady=5)

        pause_video_btn = tk.Button(self.play_video_tab, text="Pause", command=self.pause_video)
        pause_video_btn.pack(anchor=tk.CENTER, pady=5)

        stop_video_btn = tk.Button(self.play_video_tab, text="Stop", command=self.stop_video)
        stop_video_btn.pack(anchor=tk.CENTER, pady=5)

    def list_videos_clicked(self):
        video_list = lib.list_all()
        self.set_text(self.list_txt, video_list)
        self.status_lbl_check.configure(text="List Videos button was clicked!")

    def check_video_clicked(self):
        key = self.input_txt_check.get()
        name = lib.get_name(key)
        if name:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            self.set_text(self.video_txt, video_details)

            # Display the associated image
            image_path = lib.get_image_path(key)
            if image_path:
                img = Image.open(image_path)
                img = img.resize((300, 200), Image.LANCZOS)  # Updated to Image.LANCZOS
                img_tk = ImageTk.PhotoImage(img)
                self.image_lbl.config(image=img_tk)
                self.image_lbl.image = img_tk

            self.status_lbl_check.configure(text=f"Checked video {key}.")
        else:
            self.set_text(self.video_txt, f"Video {key} not found.")
            self.status_lbl_check.configure(text="Video not found.")
            self.image_lbl.config(image="")  # Clear the image label if video not found

    def play_audio(self):
        key = self.input_txt_check.get()
        media_path = lib.get_media_path(key)
        if media_path:
            pygame.mixer.music.load(media_path)
            pygame.mixer.music.play()
            self.status_lbl_check.configure(text=f"Playing audio for video {key}.")
        else:
            self.status_lbl_check.configure(text="Audio file not found.")

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.status_lbl_check.configure(text="Audio stopped.")

    def add_video_clicked(self):
        video_number = self.input_txt_playlist.get()
        if not video_number.isdigit():
            self.status_lbl_playlist.configure(text="Invalid video number. Please enter a numeric value.")
            return

        video_name = lib.get_name(video_number)
        if video_name:
            self.playlist.append(video_number)
            self.playlist_txt.insert(tk.END, f"{video_name}\n")
            self.status_lbl_playlist.configure(text=f"Added {video_name} to playlist.")
        else:
            self.status_lbl_playlist.configure(text=f"Video {video_number} not found.")

    def play_playlist_clicked(self):
        if not self.playlist:
            self.status_lbl_playlist.configure(text="Playlist is empty.")
        else:
            for video_number in self.playlist:
                lib.increment_play_count(video_number)
            self.status_lbl_playlist.configure(text="Played playlist (play counts incremented).")

    def reset_playlist_clicked(self):
        self.playlist = []
        self.playlist_txt.delete("1.0", tk.END)
        self.status_lbl_playlist.configure(text="Playlist has been reset.")

    def search_videos_clicked(self):
        search_query = self.search_txt.get().lower()
        search_results = []

        for video_number in lib.library:
            video = lib.library[video_number]
            if search_query in video.get_name().lower() or search_query in video.get_director().lower():
                search_results.append(f"{video_number}: {video.get_name()} by {video.get_director()}")

        if search_results:
            self.playlist_txt.delete("1.0", tk.END)
            for result in search_results:
                self.playlist_txt.insert(tk.END, f"{result}\n")
            self.status_lbl_playlist.configure(text=f"Found {len(search_results)} results for '{search_query}'")
        else:
            self.playlist_txt.delete("1.0", tk.END)
            self.status_lbl_playlist.configure(text=f"No results found for '{search_query}'")

    def update_rating_clicked(self):
        video_number = self.video_num_txt.get()
        new_rating = self.new_rating_txt.get()

        if not video_number.isdigit():
            self.status_lbl_update.configure(text="Invalid video number. Please enter a numeric value.")
            return

        if not new_rating.isdigit() or not (1 <= int(new_rating) <= 5):
            self.status_lbl_update.configure(text="Invalid rating. Please enter a value between 1 and 5.")
            return

        video_name = lib.get_name(video_number)
        if video_name:
            lib.set_rating(video_number, int(new_rating))
            play_count = lib.get_play_count(video_number)

            video_details = f"{video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
            self.set_text(self.video_details_txt, video_details)
            self.status_lbl_update.configure(text=f"Rating updated for {video_name}.")
        else:
            self.status_lbl_update.configure(text=f"Video {video_number} not found.")

    def open_video(self):
        self.video_source = filedialog.askopenfilename()
        if self.video_source:
            self.vid = cv2.VideoCapture(self.video_source)
            self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.canvas.config(width=self.width, height=self.height)

    def play_video(self):
        if not self.vid or not self.vid.isOpened():
            return
        self.pause = False
        self.update_video()

    def pause_video(self):
        self.pause = True

    def stop_video(self):
        self.pause = True
        self.canvas.delete("all")
        if self.vid is not None:
            self.vid.release()

    def update_video(self):
        if self.vid and self.vid.isOpened() and not self.pause:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            else:
                self.stop_video()
        self.window.after(15, self.update_video)

    @staticmethod
    def set_text(text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

if __name__ == "__main__":
    window = tk.Tk()
    VideoPlayerGUI(window)
    window.mainloop()
