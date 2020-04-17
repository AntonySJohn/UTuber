import pytube
def check(URL):
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
        print("Unfortunately, an error occured...")
    exit()

if(__name__=='__main__'):
    URL = input()
    check(URL)
