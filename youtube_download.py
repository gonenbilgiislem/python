#Youtube Video Downloader

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=bzZzXIq90I8')


cinsi = yt.fmt_streams
tipi= set(yt.streams)
size = len(cinsi)
print(size)

for i in range(0,size):
    print(tipi[i].type)
    print("")



# for i in range(0, size):
#     if cinsi[i].type == "video":
#         print(cinsi[i].type, cinsi[i].resolution, (cinsi[i].filesize) / 1024 / 1024, "MB")
#         # print(cinsi[i].url)