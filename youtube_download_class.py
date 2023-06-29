from pytube import YouTube


class YouTubeDownloader:
    resolutions = ["720p", "480p", "360p"]

    def download_video(self, url: str, resolution: str = None):
        video = YouTube(url)
        if not resolution or resolution not in self.resolutions or not video.streams.filter(resolution=resolution):
            video = video.streams.get_highest_resolution()
        else:
            video = video.streams.filter(resolution=resolution).first()
        video.download()

