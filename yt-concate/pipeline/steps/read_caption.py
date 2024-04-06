import os
from .step import Step

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt) :
                continue
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip().split(' align:')[0]
                        continue
                    elif '</c>' in line:
                        continue
                    elif time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            yt.captions = captions
            
        return data
                        
                        


