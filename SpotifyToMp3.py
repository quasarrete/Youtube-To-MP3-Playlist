from __future__ import unicode_literals
import youtube_dl, csv, re, urllib.request, datetime

#using datestamp to have unique CSV filename
timestamp = str(datetime.datetime.utcnow().timestamp())
songList = []
urls = []

#opening spotify.csv (change to whatever file required)
with open('spotify.csv') as csvfile:
#separating each line by comma and taking the first item from the row.
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
    	songList.append(row[0])

#youtube downloader settings
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

for song in songList:
    search_keyword = song.replace('"', '').replace('\'','').replace(' ','+')
    #print(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = 'https://www.youtube.com/watch?v=' + video_ids[0]
    urls.append(url)
    print('URL For: '+ song + ' is: ' + url)


try:
    #for url in urls:       
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)
except Exception:
    print("Some error occured!!")
    pass 

with open('YouTubeLink_'+ timestamp + '.csv', 'w') as myfile:
    wr = csv.writer(myfile, delimiter='\n',quoting=csv.QUOTE_NONE)
    wr.writerow(urls)