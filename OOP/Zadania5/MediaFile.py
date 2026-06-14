from abc import ABC, abstractmethod

class MediaFile(ABC):
    def __init__(self,filename, size_mb):
        self.filename = filename
        self.size_mb = size_mb
    @property
    def size_mb(self):
        return self.__size_mb
    @size_mb.setter
    def size_mb(self, value):
        if value > 0:
            self.__size_mb = value
        else:
            print("Size must be positive")
    @property
    def size_gb(self):
        return round(self.__size_mb / 1024, 4)
    @abstractmethod
    def play(self):
        pass
    def info(self):
        print(f"filename: {self.filename}, size: {self.size_mb} MB / {self.size_gb} GB")

class AudioFile(MediaFile):
    def __init__(self, filename, size_mb, duration_seconds):
        super().__init__(filename, size_mb)
        self.duration_seconds = duration_seconds
    def play(self):
        print(f"Playing audio {self.filename} ({self.duration_seconds}s)")
    
class VideoFile(MediaFile):
    def __init__(self, filename, size_mb, duration_seconds, resolution):
        super().__init__(filename, size_mb)
        self.duration_seconds = duration_seconds
        self.resolution = resolution
    def play(self):
        print(f"Playing video {self.filename} in {self.resolution} ({self.duration_seconds}s)")

class ImageFile(MediaFile):
    def __init__(self, filename, size_mb, resolution):
        super().__init__(filename, size_mb)
        self.resolution = resolution
    def play(self):
        print(f"Displaying image {self.filename} ({self.resolution})")

#TEST 
files = [
    AudioFile("podcast.mp3", 45.5, 1200),
    VideoFile("movie.mp4", 2048.0, 5400, "1920x1080"),
    ImageFile("wallpaper.png", 3.2, "3840x2160")]

for file in files:
    file.info()
    file.play()
