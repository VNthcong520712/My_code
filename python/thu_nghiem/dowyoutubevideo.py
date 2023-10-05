import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=uh_vB8N-x7A'   
youtube = pytube.YouTube(video_url) 
print(youtube) 
video = youtube.streams.first() 
print(video)
video.download('D:/Youtube')   