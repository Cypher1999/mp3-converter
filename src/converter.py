import youtube_dl

def converter(videoUrl):


    videoInfo=youtube_dl.YoutubeDL().extract_info(
        url=videoUrl, download=False
    )
    filename=f"{videoInfo['title']}.mp3"
    
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
        'postprocessor':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([videoInfo['webpage_url']])

    return filename


    