import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk  # Importing PIL for handling images
import video_library as lib  # Importing the video library module
from moviepy.editor import VideoFileClip  # Importing MoviePy for video playback


# A helper function to set text in a Tkinter Text or ScrolledText widget
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Delete existing content in the text area
    text_area.insert(1.0, content)  # Insert new content into the text area


# Class definition for the CheckVideos GUI
class CheckVideos:
    def __init__(self, window):
        # Set the dimensions and title of the window
        window.geometry("750x500")
        window.title("Check Videos")

        # Button to list all videos in the library
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Position the button on the grid

        # Label and Entry widget for entering the video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)  # Entry field for video number input
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check the details of a specific video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # ScrolledText widget to display the list of all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget to display the details of the selected video
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label to display the status of operations
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Label to display the video image
        self.image_lbl = tk.Label(window)
        self.image_lbl.grid(row=3, column=0, columnspan=4, pady=10)

        # Automatically list all videos when the GUI starts
        self.list_videos_clicked()

    # Method to handle the Check Video button click
    def check_video_clicked(self):
        key = self.input_txt.get()  # Get the video number from the input field
        name = lib.get_name(key)  # Retrieve the video name using the video number
        if name is not None:
            # If the video exists, get its details
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)  # Display video details in the text widget

            # Get the image path associated with the video
            image_path = lib.get_image_path(key)
            if image_path:
                image = Image.open(image_path)  # Open the image file
                image = image.resize((200, 150), Image.ANTIALIAS)  # Resize the image to fit the label
                photo = ImageTk.PhotoImage(image)  # Convert the image to a format Tkinter can use
                self.image_lbl.config(image=photo)  # Set the image on the label
                self.image_lbl.image = photo  # Keep a reference to avoid garbage collection
            else:
                self.image_lbl.config(image="")  # Clear the image label if no image is found

            # Play the video file associated with the video
            file_path = lib.get_file_path(key)
            if file_path:
                self.play_video(file_path)
        else:
            # If the video does not exist, display an error message
            set_text(self.video_txt, f"Video {key} not found")
            self.image_lbl.config(image="")  # Clear the image label if no video is found

        # Update the status label to indicate the Check Video button was clicked
        self.status_lbl.configure(text="Check Video button was clicked!")

    def play_video(self, file_path):
        # Play the video file using MoviePy
        video_clip = VideoFileClip(file_path)
        video_clip.preview()

    # Method to handle the List All Videos button click
    def list_videos_clicked(self):
        video_list = lib.list_all()  # Retrieve the list of all videos from the library
        set_text(self.list_txt, video_list)  # Display the video list in the ScrolledText widget
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label


# Main function to create the Tkinter window and run the CheckVideos class
if __name__ == "__main__":
    window = tk.Tk()
    CheckVideos(window)  # Create an instance of the CheckVideos class
    window.mainloop()  # Start the Tkinter event loop
