import os
from pipeline.steps.step import Step
from yt_dlp import *
import json

class DownloadCaptions(Step):
    def process(self, data, inputs):
        
        if not os.path.exists('downloadFile'):
           os.makedirs('downloadFile') 

        for url in data:
            url = str(url)
            command = f'yt-dlp --write-auto-sub --sub-lang en --skip-download --output "downloadFile/%(id)s.%(ext)s" {url}'
            os.system(command)