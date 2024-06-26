from ctypes import util
from .step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips

class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips =[]
        for found in data:
            start, end = self.process_time(found.time)
            print(found.time + found.caption)
            print(start + end)
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
            
        print('How many clips have same word: ' + str(len(clips)))

        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(utils.get_output_filepath(inputs['channel_id'], inputs['search_word']))
            
        return data
            

    def process_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)
    
    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000