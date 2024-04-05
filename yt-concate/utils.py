# utils == utilities
import os

class Utils:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_video_if_from_url(url):
        return url.split('watch?v=')[-1]
    
    def create_dirs(self):
        os.makedirs('download_dir', exist_ok = True)
        os.makedirs('download_captions', exist_ok = True)
        os.makedirs('download_videos', exist_ok = True)