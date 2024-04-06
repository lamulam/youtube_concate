from fileinput import filename
from http.client import FOUND
from .step import Step
import yt_dlp

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            if utils.video_file_exists(yt):
                print('found existing video file for ' + yt.video_filepath + ' skipping')
                continue
            
            link = yt.url
            ydl_opts = {
                'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]',  # 選擇最佳的 144p 或以下的影片格式
                'outtmpl': 'download_videos/' + yt.id + '.%(ext)s',  # 設定下載影片的儲存路徑和檔名格式
                'nooverwrites': True,  # 如果檔案已經存在，則不覆蓋檔案
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        return data