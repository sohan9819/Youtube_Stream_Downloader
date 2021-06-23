import pytube
from pytube import YouTube
from pytube import Playlist

# playlist_link = input("Enter the playlist link : ")
# link_list = Playlist(playlist_link).video_urls

# print("Playlist length : {}".format(len(link_list)))

# for link in link_list:
#     print(pytube.YouTube(link).title)
#     video = pytube.YouTube(link).streams.filter(type="audio")
#     # print(video)
#     video[0].download(r"C:\Users\sohan\Downloads\Music")

link = input("Enter the link : ")
print(pytube.YouTube(link).title)
video = pytube.YouTube(
    link).streams.filter(type="audio")
# print(video)
video[0].download(r"C:\Users\sohan\Downloads\Music")
#
