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
                'format': 'bestvideo[height<=144]+bestaudio/best[height<=144]',  # ��̨ܳΪ� 144p �ΥH�U���v���榡
                'outtmpl': 'download_videos/%(title)s.%(ext)s',  # �]�w�U���v�����x�s���|�M�ɦW�榡
                'nooverwrites': True,  # �p�G�ɮפw�g�s�b�A�h���л\�ɮ�
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        return data