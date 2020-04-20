import pytube
import os
def check1(URL):
    try:
        yt = pytube.YouTube(URL)
    except pytube.exceptions.RegexMatchError:
        print('Could not find video!!!')
    except pytube.exceptions.ExtractError:
        print ('An extraction error occurred for the video!!!')
    except pytube.exceptions.VideoUnavailable:
        print('The video is unavailable!!!')
    except KeyError:
        print('The video is blocked in your country!!!')
    except pytube.exceptions.LiveStreamError:
        print("b r u h....it's a live stream...")
    except:
        print("Unfortunately, an error occured...Check your internet connection")
    exit()

def check2(path,title):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("\nVideo with same name exists in directory!!!\n") 
        return("already exists",title)
    except FileNotFoundError:
        print("The directory entered is incorrect!!!Downloading in working directory...")
        return("",title)
    except:
        return("",title)

if(__name__=='__main__'):
    URL = input()
    check(URL)