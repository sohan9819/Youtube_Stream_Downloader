import pytube
from pytube import YouTubegit
from pytube import Playlist


def choice():
    l_type = input("What you want to download \n Link \n Playlist \n")
    link = input(
        "Download Single video or playlist \n Enter the link of the video or playlist :")

    type = input("\nSelect whether audio or video")

    if l_type.lower().strip() == "link":
        link_download(link, type)

    else:
        playlist_download(link, type)


def link_download(link, type):
    print(pytube.YouTube(link).title)
    if type.lower().strip() == "video":
        video = pytube.YouTube(link).streams.filter(progressive=True)
        print(video)
        video[1].download(r"C:\Users\sohan\Downloads\Video")
        print("\n ###### Downloaded ######## \n")
    else:
        video = pytube.YouTube(link).streams.filter(type="audio")
        print(video)
        video[0].download(r"C:\Users\sohan\Downloads\Music")
        print("\n ###### Downloaded ######## \n")


def playlist_download(link, type):
    link_list = Playlist(link).video_urls

    print("Playlist length : {}".format(len(link_list)))

    if type.lower().strip() == "audio":
        for lnk in link_list:
            print(pytube.YouTube(lnk).title)
            video = pytube.YouTube(lnk).streams.filter(type="audio")
            print(video)
            video[0].download(r"C:\Users\sohan\Downloads\Music")
            print("\n ###### Downloaded ######## \n")

    else:
        for lnk in link_list:
            print(pytube.YouTube(lnk).title)
            video = pytube.YouTube(lnk).streams.filter(progressive=True)
            print(video)
            video[1].download(r"C:\Users\sohan\Downloads\Video")
            print("\n ###### Downloaded ######## \n")


choice()
