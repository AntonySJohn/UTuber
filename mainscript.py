from pytube import YouTube
import path
import exceptions
import os
import res_fps
import playlist
def single_download(isplaylist=False,URL=None,path1=None,res_setting=None):
    resval = None
    if(isplaylist==False):
        print("Paste video URL:")
        URL = input()
    print("Please wait...\n")
    try:
        yt = YouTube(URL)
    except:
        exceptions.check1(URL,isplaylist)
    if(isplaylist==False):
        resval = res_fps.res(yt)
        path1,title0 = path.mkdirectory(yt.title)
        title = title0 + " [" + resval + "]"
        """if(path1=="already exists"):
            return()"""
        video = yt.streams.filter(file_extension="mp4",resolution=resval,progressive=True).first()
    else:
        title = path.title_check(yt.title)
        if(res_setting==2):
            video = yt.streams.filter(file_extension="mp4",progressive=True).last()
        else:
            video = yt.streams.filter(file_extension="mp4",progressive=True).first()
    #print("here")
    try:
        #print("here2")
        checkfilepath = path1+"\\"+title+".mp4"
        #print(checkfilepath)
        if(os.path.exists(checkfilepath)==False):
            if(len(path1)>0):
                video.download(path1,title)
            else:
                video.download(title)
            print("\nDownloaded",title,"!!!\n")
        else:
            print("The video",title,"already exists in this directory...\n")
    except:
        print("An unfortunate error has occured for",title,"\n")

if(__name__=='__main__'):
    print("\nThanks for using UTuber!!!\n")
    inputflag = 1
    while(inputflag!=0):
        print("Select your choice:")
        print("1.Single video")
        print("2.Playlist")
        print("3.Exit")
        choice = int(input())
        if(choice==1):
            single_download()
        elif(choice==2):
            playlist.playlist_download()
        elif(choice==3):
            print("\nThanks again!!!\n")
            exit()
        else:
            print("\nInvalid input. Please select one of the integers displayed\n")



