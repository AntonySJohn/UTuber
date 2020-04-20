import os
import exceptions
from pytube import YouTube

def title_check(title_):
    for i in range(len(title_)):
        c = title_[i]
        if(c=="\\" or c=='/' or c==':' or c=='*' or c=='?' or c== '"'or c=='<' or c=='>' or c=='|'):
            print("There is an exceptional character in the title of the video. Enter custom title...")
            title_ = input()
            break
    return(title_)

def mkdirectory(title0,isplaylist=False):
    title = title_check(title0)
    print("Would you prefer a custom download directory for the video file?(Y/N)")
    customdir = input()
    if(customdir=='Y' or customdir=='y'):
        print("Where would you like to download to?")
        path0 = input()
    else:
        path0 = 'UTuber'
    try:
        os.mkdir(path0)
    except:
        pass
    path = path0+"\\"+title
    try:
        os.mkdir(path)
    except:
        path,title = exceptions.check2(path,title,isplaylist)
    return(path,title)

if (__name__=='__main__'):
    URL = input()
    yt = YouTube(URL)
    playlistname = ""
    path0,title=mkdirectory(yt.title)
    print(path0,"\n",title)