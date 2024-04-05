import urllib.request
import json

from pipeline.steps.step import Step, StepException 
from setting import API_KEY

class GetVideoList(Step):
    def __init__(self):
        pass

    def process(self, data, inputs):
        return self.get_all_video_in_channel(inputs['channel_id'])

    def get_all_video_in_channel(self, channel_id):
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, channel_id)

        video_links = []
        url = first_url
        for _ in range(1):
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
        return video_links