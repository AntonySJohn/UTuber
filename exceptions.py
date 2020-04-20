import pytube
import os
def check1(URL,isplaylist=False):
    try:
        if(isplaylist==False):
            yt = pytube.YouTube(URL)
        else:
            yt = pytube.Playlist(URL)
    except pytube.exceptions.RegexMatchError:
        print('URL could not be found!!!')
    except pytube.exceptions.ExtractError:
        print ('An extraction error occurred!!!')
    except pytube.exceptions.VideoUnavailable:
        print('The video is unavailable!!!')
    except KeyError:
        print('The video is blocked in your country!!!')
    except pytube.exceptions.LiveStreamError:
        print("b r u h....it's a live stream...")
    except:
        print("Unfortunately, an error occured...Check your internet connection")
    if(isplaylist==False):
        exit()

def check2(path,title,isplaylist=False):
    try:
        os.mkdir(path)
    except FileExistsError:
        return(path,title)
    except FileNotFoundError:
        print("The directory entered is incorrect!!!Downloading in working directory...")
        return("",title)
    except:
        return("",title)

if(__name__=='__main__'):
    URL = input()
    check(URL)
