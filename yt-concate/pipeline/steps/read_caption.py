import os
from .step import Step

class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir('download_captions'):
            captions = {}
            with open(os.path.join('download_captions\\', caption_file) , 'r') as f:
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
            data[caption_file] = captions
            
        return data
                        
                        


