from pytube import YouTube
import os
print("Paste video URL:")
URL = input()
#yt = YouTube("https://www.youtube.com/watch?v=nE0iffq9p0o")
yt = YouTube(URL)
title = yt.title
path0 = 'videotests/Utuber'
#path0 = 'C:/Users/Antony S John/Downloads/Utuber'
try:
    os.mkdir(path0)
except:
    pass
path = path0+'/'+title
"""try:
    os.mkdir(path)
except:
    pass"""
#path2 = 'C:/Users/Antony S John/Downloads/Utuber/'+title
#print(yt.streams.all())
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

#os.mkdir(path)
#for i in range(len(list)):
 #   print(list[i])
#list.download(path)
#os.mk