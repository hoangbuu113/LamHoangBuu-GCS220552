import tkinter as tk
import video_library as lib

class UpdateVideos:
    def __init__(self, window):
        window.geometry("500x300")
        window.title("Update Video Rating")

        video_num_lbl = tk.Label(window, text="Enter Video Number")
        video_num_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.video_num_txt = tk.Entry(window, width=5)
        self.video_num_txt.grid(row=0, column=1, padx=10, pady=10)

        new_rating_lbl = tk.Label(window, text="Enter New Rating")
        new_rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_txt = tk.Entry(window, width=5)
        self.new_rating_txt.grid(row=1, column=1, padx=10, pady=10)

        update_rating_btn = tk.Button(window, text="Update Rating", command=self.update_rating_clicked)
        update_rating_btn.grid(row=2, column=0, padx=10, pady=10)

        self.video_details_txt = tk.Text(window, width=40, height=4, wrap="none")
        self.video_details_txt.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=2, sticky="W", padx=10, pady=10)

    def update_rating_clicked(self):
        video_number = self.video_num_txt.get()
        new_rating = self.new_rating_txt.get()

        if not video_number.isdigit():
            self.status_lbl.configure(text="Invalid video number. Please enter a numeric value.")
            return

        if not new_rating.isdigit() or not (1 <= int(new_rating) <= 5):
            self.status_lbl.configure(text="Invalid rating. Please enter a value between 1 and 5.")
            return

        video_name = lib.get_name(video_number)
        if video_name is not None:
            lib.set_rating(video_number, int(new_rating))
            play_count = lib.get_play_count(video_number)

            video_details = f"{video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
            self.video_details_txt.delete("1.0", tk.END)
            self.video_details_txt.insert(tk.END, video_details)
            self.status_lbl.configure(text=f"Rating updated for {video_name}.")
        else:
            self.status_lbl.configure(text=f"Video {video_number} not found.")

if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideos(window)
    window.mainloop()
