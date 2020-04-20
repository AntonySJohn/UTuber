from pytube import YouTube
import random
def res(obj):
    available_resolutions = []
    resolutions=["2160p","1440p","1080p","720p","360p","240p","144p"]
    print("\nUnfortunately, we can only provide limited resolutions due to certain technical difficulties...\n")
    print("Select desired resolutions:")
    for i in range(len(resolutions)):
        temp = obj
        if(len(temp.streams.filter(res=resolutions[i],file_extension='mp4',progressive=True))>0):
            available_resolutions.append(i)
            print(len(available_resolutions),". ",resolutions[i])
    try:
        index = available_resolutions[int(input())-1]
    except:
        print("\nOh, we got a comedian here...So, 1080p right?")
        index = available_resolutions[len(available_resolutions)-1]
    return(resolutions[index])
if(__name__=='__main__'):
    URL = input()
    yt = YouTube(URL)
    res(yt)