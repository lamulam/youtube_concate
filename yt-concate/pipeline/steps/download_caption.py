import os
from pipeline.steps.step import Step
from yt_dlp import *
import json
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if utils.caption_file_exists(yt):
                print('Found existing caption')
                continue
            else:
                print('downloading new caption file.')
                
            try:
                command = f'yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs srt --output "download_captions/%(id)s.%(ext)s" {yt.url}'
            except:
                print('downloading error')
            os.system(command)

        return data

