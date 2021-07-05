from pytube import YouTube
SAVE_PATH = "C:/"
link="https://www.youtube.com/watch?v=xWOoBJUqlbM"

try:
    yt = YouTube(link) 
except: 
    print("Connection Error")
mp4files = yt.filter('mp4')
yt.set_filename('nice Video')  
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
  d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 
  
  