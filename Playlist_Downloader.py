import pytube
from pytube import Playlist
from pytube import YouTube

main_link = input("Enter the link of the playlist : ")
n = int(input("Enter number of videos : "))
playlist = Playlist(main_link)
print("#########  {}  #########" .format(playlist.title))

### select number of videos ###
if n == 0:
    playlist_Links = playlist.video_urls
else:
    playlist_Links = playlist.video_urls[:n]
# playlist_Links = playlist.video_urls

    ### display number of videos ###
print("Number of videos  : {}".format(len(playlist_Links)))
# print(playlist_Links)

### select video quality #####
temp = YouTube(playlist_Links[1]).streams.filter(progressive=True).all()
for strm in temp:
    print("{} : {}".format(temp.index(strm), strm))
# print(YouTube(playlist_Links[1]).streams)
q = int(input("\n Enter the serial number of the required stream : "))


def download_all(play_list, n):
    i = 1
    for link in play_list:
        if i < len(play_list)+1 and i >= 13:
            # if i <= len(play_list):
            print(i)
            i += 1
            print(YouTube(link).streams[n])
            # HD quality
            # yt = YouTube(link).streams[n].download(r"C:\Users\sohan\Downloads\testing")
            yt = pytube.YouTube(link)
            vd = pytube.YouTube(link).streams.filter(progressive=True)

            # Title of the Video

            print("Title: " + yt.title)
            title = yt.title

            # # Length of the Video in Seconds

            # print("Duration: " + str(yt.length))

            # # URL of the Thumbnail of the video

            # print("Thumbnail Link: " + yt.thumbnail_url)

            # Description of the Video

            print("Description: " + yt.description)
            description = yt.description

            # # Total Views of the Video

            # print("Views: " + str(yt.views))

            # # Age Restricted Content

            # print("Age Restricted: " + str(yt.age_restricted))

            # # ID of the Video

            # print("Video ID: " + yt.video_id)

            f = open(
                r"C:\Users\sohan\Downloads\Kavien_Powell_Grid_Portfolio\Info.txt", "a+", encoding='utf-8')
            f.write("Title : {}\n{}\n\n################################################\n\n".format(
                title, description))
            f.close()

            try:
                video = vd[n].download(
                    r"C:\Users\sohan\Downloads\Kavien_Powell_Grid_Portfolio")
            except:
                video = vd[n].download(
                    r"C:\Users\sohan\Downloads\Kavien_Powell_Grid_Portfolio")

            # video = vd[n].download(
            #     r"S:\Learning_Section(Tutorials)\C++_Full_Youtube_Playlist")

            print('\n##########  Download is complete of video {}  #############\n'.format(
                yt.title))

        else:
            i += 1
            continue


download_all(playlist_Links, q)
