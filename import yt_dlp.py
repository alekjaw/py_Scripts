import yt_dlp

url = 'https://www.youtube.com/watch?v=1D6RqvT4t2o'

ydl_opts = {
    'format': 'best',
    'outtmpl': r'C:\Users\Alek\Desktop\HEMISYNC.MP4',
    'noplaylist': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])