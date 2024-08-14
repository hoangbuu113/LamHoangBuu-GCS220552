import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib


class CreateVideoList:
    def __init__(self, window):
        window.geometry("600x450")
        window.title("Create Video List")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_video_clicked)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        search_lbl = tk.Label(window, text="Search (by Name or Director)")
        search_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.search_txt = tk.Entry(window, width=20)
        self.search_txt.grid(row=1, column=1, padx=10, pady=10)

        search_btn = tk.Button(window, text="Search", command=self.search_videos_clicked)
        search_btn.grid(row=1, column=2, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(window, width=50, height=15, wrap="none")
        self.playlist_txt.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_btn.grid(row=3, column=0, padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_btn.grid(row=3, column=1, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.playlist = []

    def add_video_clicked(self):
        video_number = self.input_txt.get()

        if not video_number.isdigit():
            self.status_lbl.configure(text="Invalid video number. Please enter a numeric value.")
            return

        video_name = lib.get_name(video_number)
        if video_name is not None:
            self.playlist.append(video_number)
            self.playlist_txt.insert(tk.END, f"{video_name}\n")
            self.status_lbl.configure(text=f"Added {video_name} to playlist.")
        else:
            self.status_lbl.configure(text=f"Video {video_number} not found.")

    def play_playlist_clicked(self):
        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty.")
        else:
            for video_number in self.playlist:
                lib.increment_play_count(video_number)
            self.status_lbl.configure(text="Played playlist (play counts incremented).")

    def reset_playlist_clicked(self):
        self.playlist = []
        self.playlist_txt.delete("1.0", tk.END)
        self.status_lbl.configure(text="Playlist has been reset.")

    def search_videos_clicked(self):
        search_query = self.search_txt.get().lower()
        search_results = []

        for video in lib.videos:
            if search_query in video.name.lower() or search_query in video.director.lower():
                search_results.append(f"{video.video_number}: {video.name} by {video.director}")

        if search_results:
            self.playlist_txt.delete("1.0", tk.END)
            for result in search_results:
                self.playlist_txt.insert(tk.END, f"{result}\n")
            self.status_lbl.configure(text=f"Found {len(search_results)} results for '{search_query}'")
        else:
            self.playlist_txt.delete("1.0", tk.END)
            self.status_lbl.configure(text=f"No results found for '{search_query}'")


if __name__ == "__main__":
    window = tk.Tk()
    CreateVideoList(window)
    window.mainloop()
