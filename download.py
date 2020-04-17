from pytube import YouTube
import os
print("Paste video URL:")
URL = input()
yt = YouTube(URL)
title = yt.title
path0 = 'videotests/UTuber'
try:
    os.mkdir(path0)
except:
    pass
path = path0+'/'+title
list = yt.streams.filter(progressive=True,file_extension="mp4").first()
flag = 1
try:
    os.mkdir(path)
except:
    check = path+'/'+title+'.mp4'
    if(os.path.isfile(check)):
        print("\nVideo with same name exists in directory!!!\n")
        flag = 0
if(list.download(path) and flag==1):
    print("\nDownload success!!!\n")
