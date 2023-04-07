# YOUTUBE TO MP3 DOWNLOADER
Simple <a href="https://www.python.org/" target="_blank">Python</a> script (implemented via <a href="https://www.jetbrains.com/pycharm/" target="_blank">PyCharm</a> IDE) for downloading mp3 songs from youtube. The Script requires you to enter the youtube playlist link from which it will download the songs, after that the path where them will be saved. If the path is non-existent, the script will create the folder and save the songs into that.

The Script requires several external packages:
- pytube
- pydub (which requires libav first)
- moviepy

## INSTALLATION INSTRUCTIONS

### libav

1. Download it from [here (windows 64bit).](https://drive.google.com/file/d/1Ua1hXPnSWHBOLK_uCV4OqyRE7_QFXa8R/view?usp=sharing) For other versions, check [here.](http://builds.libav.org/windows/release-gpl/)
2. Add the libav ```/bin``` folder to your PATH environment variables
3. After that, you can use the pydub package

### Python Packages
Simply run ```pip install``` followed by the package name

```
pip install pytube
pip install pydub
pip install moviepy
```