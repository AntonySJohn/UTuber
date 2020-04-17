from pytube import YouTube
import path
import exceptions
import os
import res_fps
print("Paste video URL:")
URL = input()
print("Please wait...")
try:
    yt = YouTube(URL)
except:
    exceptions.check(URL)
#resval,fpsval = res(yt)
resval = res_fps.res(yt)
video = yt.streams.filter(file_extension="mp4",resolution=resval).first()
path = path.mkdir(yt)
if(path=="already exits"):
    exit()
if(video.download(path)):
    print("\nDownload success!!!\n")
else:
    print("An unfortunate error has occured...\n")

