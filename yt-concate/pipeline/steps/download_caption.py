import os
from pipeline.steps.step import Step
from yt_dlp import *
import json
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            
            url = str(url)
            if utils.caption_file_exists(url):
                print('Found existing caption')
                continue
            else:
                print('downloading new caption file.')
                
          
            command = f'yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs srt --output "download_captions/%(id)s.%(ext)s" {url}'
            os.system(command)
        end = time.time()  

