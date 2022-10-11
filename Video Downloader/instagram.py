from pytube import YouTube
from instascrape import Reel
import time
import os
import datetime
import os
os.chdir(f"E:/Youtube Videos")
path = f"E:/Youtube Videos/{str(datetime.date.today())}"
isdir = os.path.isdir(path)
if not isdir:
    os.makedirs(str(datetime.date.today()))
os.chdir(f"E:/Youtube Videos/{str(datetime.date.today())}")

it_url_list = ["https://www.instagram.com/reel/CVkN-too8Cc/?utm_source=ig_web_copy_link",
                       "https://www.instagram.com/reel/CbFQ1xsopWL/?utm_source=ig_web_copy_link"]
SESSIONID = "180bce934a4-2393eb"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
            "cookie": f'sessionid={SESSIONID};'
        }
it_url_list = it_url_list
for i in it_url_list:
    my_reel = Reel(i)
    my_reel.scrape(headers=headers)
    my_reel.download(fp=f"reel{int(time.time())}.mp4")
print("Reels Download Complete")
