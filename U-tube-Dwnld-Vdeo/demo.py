from pytube import YouTube

link = "https://www.youtube.com/watch?v=G6NVxIKyMEQ"
youtube_1 = YouTube(link)

videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter : ")) 
videos[strm].download()
print("Successfully")   