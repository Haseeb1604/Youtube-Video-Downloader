from pytube import YouTube

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA"

video = YouTube(url)

# Return Resolutions list
def getResolutions(video):
    res = set([int(i.resolution[:-1]) for i in video.streams.order_by('resolution')])
    return sorted(res, reverse=True)

# Get Filtered Video
video.streams.filter(res="360p", progressive=True, mime_type="video/mp4")
