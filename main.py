import os
from pytube import YouTube
from pytube import Playlist
from pydub import AudioSegment
import moviepy.editor as mp
import re

username = os.getlogin()

link = input("Insert the Playlist link to download to (Playlist must be Public or Not Listed): ")
playlist = Playlist(link)

initial_path = '/Users/' + username + '/Desktop/'
download_path = initial_path + input("Enter the path where to save the songs: C" + initial_path)

if not os.path.exists(download_path):
    os.makedirs(download_path)
    print("Non-Existent Path, Folder Created at: " + download_path)

print("==============================================================================================================")
print("Playlist " + playlist.title + " with " + str(playlist.length) + " songs found, proceed to download...")
print("==============================================================================================================")

not_downloaded = True

for url in playlist:
    youtube_title = YouTube(url).title
    for file in os.listdir(download_path):
        if youtube_title+'.mp3' == file:
            print("Track " + youtube_title + " already downloaded, skipped")
            not_downloaded = False
    if not_downloaded:
        print("Downloading Track: " + youtube_title + "...")
        YouTube(url).streams.get_audio_only().download(download_path,youtube_title+'.mp4')
        # YouTube(url).streams.filter(only_audio=True).first().download(download_path)
    not_downloaded = True

for file in os.listdir(download_path):
    if re.search('mp4', file):
        mp4_path = os.path.join(download_path,file)
        mp3_path = os.path.join(download_path,os.path.splitext(file)[0]+'.mp3')
        if not os.path.exists(mp3_path):
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            AudioSegment.from_file(mp3_path).export(mp3_path, format="mp3", bitrate="320k")
            new_file.close()
        os.remove(mp4_path)