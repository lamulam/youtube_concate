from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_videolist import GetVideoList, StepException
from pipeline.steps.initialize_yt import InitializeYT
from pipeline.steps.download_caption import DownloadCaptions
from pipeline.steps.read_caption import ReadCaption
from pipeline.steps.search import Search
from pipeline.steps.download_videos import DownloadVideos
from pipeline.steps.postflight import Postflight
from utils import Utils

CHANNEL_ID = 'UCkr5nkb4_jvvEeSY9POqqtQ'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'Trident',
        }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
        ]
    
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)
    
if __name__ == '__main__':
    main()