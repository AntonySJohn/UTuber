import os
from pytube import YouTube
def mkdir(obj,playlistname="",fileformat='.mp4'):
    title = obj.title
    print("Would you prefer a custom download directory?(Y/N)")
    customdir = input()
    if(customdir=='Y' or customdir=='y'):
        print("Enter path")
        path0 = input()
        print(path0)
    else:
        path0 = 'videotests/UTuber'
    if(len(playlistname)>0):
        path0 = path0+'/'+playlistname
        path = path0+'/'
    else:
        path = path0+'/'+title
        print(path)
    try:
        os.mkdir(path)
    except:
        check = path+'/'+title+fileformat
        if(os.path.isfile(check)):
            print("\nVideo with same name exists in directory!!!\n")    
            return("already exits")
    return(path)

if (__name__=='__main__'):
    URL = input()
    yt = YouTube(URL)
    playlistname = input()
    mkdir(yt,playlistname)
    
