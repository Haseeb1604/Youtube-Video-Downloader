from pytube import YouTube

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA"

video = YouTube(url)

# print(video.title)
# print(video.thumbnail_url)

vid = video.streams.all()
# print(vid)

for i in vid:
    print(i)
