from __future__ import unicode_literals
import youtube_dl
import os

URLS_FILE_NAME = 'example.txt'
URLS_FILE = os.path.join('urls', URLS_FILE_NAME)
SAVE_DIRECTORY = '~/Desktop/download'


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '{}/%(title)s.%(ext)s'.format(SAVE_DIRECTORY)
}

with open(URLS_FILE, 'r') as urls_file:
    for url in urls_file:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url.strip()])
