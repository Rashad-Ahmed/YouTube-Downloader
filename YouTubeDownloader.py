from pytube import YouTube

link = input("Paste the video link:\n")
yt = YouTube(link)

data = {
    'Title': yt.title,
    'Number of views': yt.views,
    'Length of video': yt.length,
    'rating of video': yt.rating
}

for k, v in data.items():
    print(k, ":", v)


highRes = yt.streams.get_highest_resolution()
print("downloading...")
highRes.download()
print("Download completed!!!")
