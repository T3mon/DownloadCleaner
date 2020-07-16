from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    @staticmethod
    def to_file(filename, dest):
        file = folder_from + "/" + filename
        new_path = dest + "/" + filename
        os.rename(file, new_path)

    def on_modified(self, event):
        for filename in os.listdir(folder_from):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png"
                                       or extension[1].lower() == "jpeg"):
                self.to_file(filename, folder_to_img)
            elif len(extension) > 1 and (extension[1].lower() == "mp3" or extension[1].lower() == "mp4"
                                         or extension[1].lower() == "wav" or extension[1].lower() == "mpeg"):
                self.to_file(filename, folder_to_audio)
            elif len(extension) > 1 and (extension[1].lower() == "doc" or extension[1].lower() == "pdf"
                                         or extension[1].lower() == "tex " or extension[1].lower() == "wpd"
                                         or extension[1].lower() == "docx" or extension[1].lower() == "txt"
                                         or extension[1].lower() == "rtf" or extension[1].lower() == "wpd"):
                self.to_file(filename, folder_to_text)


username = "Артем"

folder_from = "C:/Users/" + username + "/Downloads"
folder_to_img = "C:/Users/" + username + "/Desktop/img"
folder_to_audio = "C:/Users/" + username + "/Desktop/audio"
folder_to_text = "C:/Users/" + username + "/Desktop/text"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_from, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
