from pytube import YouTube
from sys import argv
import os

download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
link = argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Download folder: ", download_dir)

yd = yt.streams.get_highest_resolution()
yd.download(download_dir)
