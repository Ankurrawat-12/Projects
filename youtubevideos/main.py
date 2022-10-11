from pytube import YouTube
from instascrape import Reel
import time
import os

os.chdir(r"E:\Youtube Videos")

# YouTube Shots
yt_url_list = [""]
yt_name_list = []
thumbnail_list = []
yt_info = {
    "Url": yt_url_list,
    "Name": yt_name_list,
    "Thumbnail": thumbnail_list
}

for i in yt_url_list:
    my_shot = YouTube(i)
    yt_name_list.append(my_shot.title)
    thumbnail_list.append(my_shot.thumbnail_url)
    # my_shot = my_shot.streams.get_highest_resolution()
    # my_shot.download()

print(yt_info)

