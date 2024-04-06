# utils == utilities
import os

class Utils:
    def __init__(self) -> None:
        pass
    
    def create_dirs(self):
        os.makedirs('output_dir', exist_ok = True)
        os.makedirs('download_captions', exist_ok = True)
        os.makedirs('download_videos', exist_ok = True)
        
    def caption_file_exists(self, yt):
        path = yt.caption_filepath
        return os.path.exists(path) and os.path.getsize(path) > 0
 
    def video_file_exists(self, yt):
        path = yt.video_filepath
        return os.path.exists(path) and os.path.getsize(path) > 0
   
    def get_video_list_filepath(self, channel_id):
        return os.path.join('download_captions', channel_id + '.txt')
    
    def video_list_file_exists(self, yt):
        return os.path.exists(yt.caption_filepath) and os.path.getsize(yt.caption_filepath) > 0

    def video_list_exists(self, channel_id):
        path = os.path.join('download_captions', channel_id + '.txt')
        return os.path.exists(path)
    
    def get_output_filepath(self, channel_id, search_word):
        return os.path.join('output_dir', channel_id + '_' + search_word + '.mp4')



