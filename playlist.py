from pytube import Playlist,YouTube
import path
import random
import mainscript
import exceptions
def playlist_download():
    res_setting = 0
    res_flag=1
    dumbpeople=["Quit playin around\n","I aint got all day\n"]
    print("\nPaste playlist URL:")
    URL = input()
    print("Please wait...\n")
    try:
        playlist = Playlist(URL)
    except:
        exceptions.check1(URL,True)
    URL_list = playlist.video_urls
    while(res_flag==1):
        print("Which resolution setting would you prefer?:")
        print("1.Download in highest available resolution")
        print("2.Download in lowest available resolution")
        res_setting = int(input())
        if(res_setting!=1 and res_setting!=2):
            print(dumbpeople[random.choice([0,1])])
        else:
            if(res_setting==1):
                title = playlist.title() + "[High res]"
            else:
                title = playlist.title() + "[Low res]"
            res_flag=0
    path1,title = path.mkdirectory(title,True)
    for video in URL_list:
        mainscript.single_download(True,video,path1,res_setting)
    print("Finished")

if(__name__=="__main__"):
    playlist_download()