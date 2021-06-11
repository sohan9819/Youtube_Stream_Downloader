import pytube
from pytube import YouTube

link = input("Enter the link : ")
title = pytube.YouTube(link).title
description = pytube.YouTube(link).description
f = open(
    r"S:\Learning_Section(Tutorials)\C++_Beginners\Info.txt", "a+", encoding='utf-8')
f.write("Title : {}\n{}\n\n################################################\n\n".format(
    title, description))
f.close()
yt = pytube.YouTube(link).streams.filter(progressive=True)
i = 0
for s in yt:
    print("{}:{}".format(i, s))
    i += 1

s_no = int(input("Enter the stream no : "))
# audio = yt[s_no].download(r"C:\Users\sohan\Music\Coding_Chill_beats")
# audio = yt.last().download(r"C:\Users\sohan\Music\Coding_Chill_beats")
video = yt[s_no].download(r"S:\Learning_Section(Tutorials)\C++_Beginners")
