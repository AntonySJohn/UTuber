import os
import exceptions
from pytube import YouTube
def mkdirectory(obj,playlistname="",fileformat='.mp4'):
    title = obj.title
    for i in range(len(title)):
        c = title[i]
        if(c=="\\" or c=='/' or c==':' or c=='*' or c=='?' or c== '"'or c=='<' or c=='>' or c=='|'):
            print("There is an exceptional character in the title of the video. Enter custom title...")
            title = input()
            break
    print("Would you prefer a custom download directory for the video file?(Y/N)")
    customdir = input()
    #print(customdir)
    if(customdir=='Y' or customdir=='y'):
        print("Where would you like to download to?")
        path0 = input()
        #print(path0)
    else:
        path0 = 'videotests\\UTuber'
    try:
        os.mkdir(path0)
    except:
        pass
    if(len(playlistname)>0):
        path0 = path0+'\\'+playlistname
        path = path0+'\\'
    else:
        path = path0+'\\'+title
    #os.mkdir(path)
    try:
        os.mkdir(path)
    except:
        exceptions.check2(path,title)
    return(path,title)

if (__name__=='__main__'):
    URL = input()
    yt = YouTube(URL)
    playlistname = ""
    #playlistname = input()
    path0,title=mkdirectory(yt,playlistname)
    print(path0,"\n",title)
    
