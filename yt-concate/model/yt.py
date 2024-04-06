import os

class YT:
    def __init__(self, url):
        self.url = str(url)
        self.id = self.get_video_if_from_url(self.url)
        self.caption_filepath = os.path.join('download_captions', self.id + '.en.srt')
        self.video_filepath = os.path.join('download_videos', self.id + '.webm')
        self.captions = None


    @staticmethod
    def get_video_if_from_url(url):
        return url.split('watch?v=')[-1]
    
    def __str__(self):
        return '<YT(yt=' + str(self.yt) + ')>'
    
    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath)            
            ])
        return '<YT(' + content + '>'