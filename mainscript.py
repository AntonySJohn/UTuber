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
    exceptions.check1(URL)
resval = res_fps.res(yt)
video = yt.streams.filter(file_extension="mp4",resolution=resval,).first()
path1,title = path.mkdirectory(yt)
if(path1=="already exists"):
    exit()
try:
    if(len(path1)>0):
        video.download(path1,title)
    else:
        video.download(title)
    print("\nDownload success!!!")
except:
    print("An unfortunate error has occured...\n")

