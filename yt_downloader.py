from moviepy.editor import *
from pytube import YouTube
import os
import time
import tkinter as tk

def main():

    def download():
        
        global link
        global path_folder
        global filename
        url = link
        path = path_folder
        video = YouTube(url).streams.first()
        video.download(path)

        mp4_file = r"{}\YouTube.mp4".format(path)
        mp3_file = r"{}\{}.mp3".format(path, filename)

        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()
        os.remove(mp4_file)

    def get_link():
        global link
        link = link_entry.get()
        link_entry.delete(first = 0, last = len(link))

    def get_folder():
        global path_folder
        path_folder = folder_entry.get()
        folder_entry.delete(first = 0, last = len(path_folder))

    def get_filename():
        global filename
        filename = filename_entry.get()
        filename_entry.delete(first = 0, last = len(filename))


    link = ""
    path_folder = ""
    filename = ""
    window = tk.Tk()
    window.title("Youtube Downloader")
    canvas = tk.Canvas(window, width = 300, height = 450)
    canvas.pack()

    name_label = tk.Label(window, text = "Youtube Downloader", fg = "red", font = ("helvetica", 20, "bold"))
    done_label = tk.Label(window, text = "Downloading is done !", fg = "green", font = ("helvetica", 17, "bold"))

    link_label = tk.Label(window, text = "Your link", fg = "green", font= ("helvetica", 15, "bold"))
    link_entry = tk.Entry(window)
    link_button = tk.Button(window, text="Enter link", width=17, command = get_link)

    folder_label = tk.Label(window, text = "Your folder", fg = "green", font = ("helvatica", 15, "bold"))
    folder_entry = tk.Entry(window)
    folder_button = tk.Button(window, text="Enter folder", width=17, command = get_folder)

    filename_label = tk.Label(window, text = "Enter filename", fg = "green", font = ("helvetica", 15, "bold"))
    filename_entry = tk.Entry(window)
    filename_button = tk.Button(window, text = "Enter folder", width = 17, command = get_filename)

    download_button = tk.Button( text="Download", bg = "brown", fg = "white", font = ("helvetica", 15, "bold"), command = download)

    canvas.create_window(150, 20, window = name_label)

    canvas.create_window(150, 60, window = link_label)
    canvas.create_window(150, 85, window = link_entry)
    canvas.create_window(150, 120, window = link_button)

    canvas.create_window(150, 170, window = folder_label)
    canvas.create_window(150, 200, window = folder_entry)
    canvas.create_window(150, 230, window = folder_button)

    canvas.create_window(150, 260, window = filename_label)
    canvas.create_window(150, 290, window = filename_entry)
    canvas.create_window(150, 320, window = filename_button)

    canvas.create_window(150, 370, window = download_button)

    window.mainloop()

if __name__ == "__main__":
    main()
