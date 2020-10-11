# YouTube-To-MP3
Using spotify playlist to download music from YouTube and save as MP3

# pre req
All of the following packages are required to be installed.
# unicode_literals, youtube_dl, csv, re, urllib.request, datetime

# How to get the playlist
First of all you need to find your favourite playlist from wherever. Spotify is a good place to start.
Once you get the playlist, get the link. Use some website to download it as CSV file. 
# Good idea to save the file as Spotify.csv

https://www.tunemymusic.com/Spotify-to-File.php is a good place to start.

# Configure Python file

Modifiy the SpotifyToMp3.py file to include your Spotify playlist CSV file.
Easier to save the file as 

Make sure new title is on first column of each row. e.g. A1, B1, C1, D1. (Spotify playlist might have other information in different columns, ignore those) 

# Download

Once the playlist file is included in the .py , you can run the script. This should automatically search youtube and start downloading the first item from each search result.

# YoutubeDL

MP3 is downloaded using YouTubeDL : https://ytdl-org.github.io/youtube-dl/index.html
Please have a  look at their documentation is something doesn't work correctly.
