from pytube import YouTube
from instascrape import Reel
import time
import datetime
import os

os.chdir(f"E:/Youtube Videos")

path = f"E:/Youtube Videos/{str(datetime.date.today())}"
isdir = os.path.isdir(path)
if not isdir:
    os.makedirs(str(datetime.date.today()))
os.chdir(f"E:/Youtube Videos/{str(datetime.date.today())}")
SESSIONID = "180bce934a4-2393eb"

yt_url_list = ["https://youtube.com/shorts/4awgbpipCHg?feature=share",
               "https://youtube.com/shorts/5o97doW4D3c?feature=share",
               "https://youtube.com/shorts/5uHK4kfY310?feature=share",
               "https://youtube.com/shorts/tzZ8TDBbRAQ?feature=share",
               "https://youtube.com/shorts/Gq2rTkzAiAE?feature=share",
               "https://youtube.com/shorts/zxwBCF-kg34?feature=share",
               "https://youtube.com/shorts/6SCIvgVbY3U?feature=share",
               "https://youtube.com/shorts/okCD6aHbf9E?feature=share",
               "https://youtube.com/shorts/GT7kYR_qerg?feature=share",
               "https://youtube.com/shorts/5YNdLeGLUgs?feature=share",
               "https://youtube.com/shorts/X-8FRKvP2Fs?feature=share",
               "https://youtube.com/shorts/QzaUP7xzE38?feature=share"]
it_url_list = ["https://www.instagram.com/reel/CVkN-too8Cc/?utm_source=ig_web_copy_link",
                "https://www.instagram.com/reel/CbFQ1xsopWL/?utm_source=ig_web_copy_link"]


class VideoDownloader:
    def __init__(self):
        self.yt_url_list = []
        self.yt_name_list = []
        self.thumbnail_list = []
        self.yt_info = {
            "Url": self.yt_url_list,
            "Name": self.yt_name_list,
            "Thumbnail": self.thumbnail_list
        }
        self.it_url_list = []


        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
            "cookie": f'sessionid={SESSIONID};'
        }

    # def

    def Shots(self, yt_url_list):
        self.yt_url_list = yt_url_list
        for i in self.yt_url_list:
            my_shot = YouTube(i)
            self.yt_name_list.append(my_shot.title)
            self.thumbnail_list.append(my_shot.thumbnail_url)
            my_shot = my_shot.streams.get_highest_resolution()
            my_shot.download()
        print("Shots Download Complete")

    def Reels(self, it_url_list):
        self.it_url_list = it_url_list
        for i in self.it_url_list:
            my_reel = Reel(i)
            my_reel.scrape(headers=self.headers)
            my_reel.download(fp=f"reel{int(time.time())}.mp4")
        print("Reels Download Complete")


downloader = VideoDownloader()
downloader.Shots(yt_url_list)
# downloader.Reels(it_url_list)
