class LibraryItem:
    def __init__(self, video_number, name, director, rating, play_count, image_path=None, media_path=None):
        self.video_number = video_number
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count
        self.image_path = image_path
        self.media_path = media_path

    def get_name(self):
        return self.name

    def get_director(self):
        return self.director

    def get_rating(self):
        return self.rating

    def set_rating(self, new_rating):
        self.rating = new_rating

    def get_play_count(self):
        return self.play_count

    def increment_play_count(self):
        self.play_count += 1

    def get_image_path(self):
        return self.image_path

    def get_media_path(self):
        return self.media_path

    def to_dict(self):
        return {
            "video_number": self.video_number,
            "name": self.name,
            "director": self.director,
            "rating": self.rating,
            "play_count": self.play_count,
            "image_path": self.image_path,
            "media_path": self.media_path
        }

# Example video library items with paths pointing to the 'csv' folder
library = {
    "01": LibraryItem("01", "Don't let you go", "GUrbane ft. Phuc Nam", 4, 0, "0.jpg",
                      "y2mate.com - 5 Dont let you go  GUrbane ft Phuc Nam Official Audio.mp3"),
    "02": LibraryItem("02", "RED FLAG", "TEZ", 5, 0, "0 (1).jpg",
                      "y2mate.com - TEZ  RED FLAG  ft GILL  MASON NGUYỄN .mp3"),
    "03": LibraryItem("03", "DANCING IN THE DARK", "SOOBIN", 2, 0, "0 (2).jpg",
                      "y2mate.com - SOOBIN  DANCING IN THE DARK  BẬT NÓ LÊN Album Official Visualizer.mp3"),
    "04": LibraryItem("04", "Yêu Thương Ngày Đó", "SOOBIN", 1, 0, "0 (3).jpg",
                      "y2mate.com - Yêu Thương Ngày Đó  SOOBIN Hoàng Sơn.mp3"),
    "05": LibraryItem("05", "NEXT!", "ncts", 3, 0, "0 (4).jpg", "y2mate.com - ncts  NEXT Brazilian Phonk.mp3"),
}

def list_all():
    return "\n".join([f"{video.video_number}: {video.name} by {video.director}" for video in library.values()])

def get_name(video_number):
    return library.get(video_number).get_name() if video_number in library else None

def get_director(video_number):
    return library.get(video_number).get_director() if video_number in library else None

def get_rating(video_number):
    return library.get(video_number).get_rating() if video_number in library else None

def set_rating(video_number, new_rating):
    if video_number in library:
        library[video_number].set_rating(new_rating)

def get_play_count(video_number):
    return library.get(video_number).get_play_count() if video_number in library else None

def increment_play_count(video_number):
    if video_number in library:
        library[video_number].increment_play_count()

def get_image_path(video_number):
    return library.get(video_number).get_image_path() if video_number in library else None

def get_media_path(video_number):
    return library.get(video_number).get_media_path() if video_number in library else None
