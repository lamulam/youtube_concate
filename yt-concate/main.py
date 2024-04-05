from pipeline.pipeline import Pipeline
from pipeline.steps.preflight import Preflight
from pipeline.steps.get_videolist import GetVideoList, StepException
from pipeline.steps.download_caption import DownloadCaptions
from pipeline.steps.postflight import Postflight
from utils import Utils

CHANNEL_ID = 'UCkr5nkb4_jvvEeSY9POqqtQ'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
        
        }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
        ]
    
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)
    
if __name__ == '__main__':
    main()