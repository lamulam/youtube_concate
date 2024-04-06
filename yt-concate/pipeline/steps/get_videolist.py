import urllib.request
import json

from pipeline.steps.step import Step, StepException 
from setting import API_KEY

class GetVideoList(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        if utils.video_list_file_exists(inputs['channel_id']):
            print('Found existing video list file for channel id', inputs['channel_id'])
            return self.read_file(utils.get_video_list_filepath(inputs['channel_id']))
        return self.get_all_video_in_channel(inputs['channel_id'], utils)

    def get_all_video_in_channel(self, channel_id, utils):
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

        video_links = []
        url = first_url
        for _ in range(2):
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
            
        print('Videos list:', video_links)
        print('Channel have ' + str(len(video_links)) + 'videos.') 
        
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links
    
    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')
                
    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:  
            for url in f:
                video_links.append(url.strip())
                
        return video_links