import os
from pipeline.steps.step import Step
from yt_dlp import *
import json

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            url = str(url)
            command = f'yt-dlp --write-auto-sub --sub-lang en --skip-download --convert-subs srt --output "download_captions/%(id)s.%(ext)s" {url}'
            os.system(command)

