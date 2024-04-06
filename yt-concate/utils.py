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
        
        
    def caption_file_exists(self, url):
        path = 'download_captions\\' + url.split('watch?v=')[-1] + '.en.vtt'
        return os.path.exists(path) and os.path.getsize(path) > 0
    
    def get_video_list_filepath(self, channel_id):
        return os.path.join('download_captions', channel_id + '.txt')
    
    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0




