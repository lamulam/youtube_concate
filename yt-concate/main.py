from pipeline.pipeline import Pipeline
from pipeline.steps.get_videolist import GetVideoList, StepException
from pipeline.steps.download_caption import DownloadCaptions

CHANNEL_ID = 'UCwaS8_S7kMiKA3izlTWHbQg'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
        
        }

    steps = [
        GetVideoList(),
        DownloadCaptions(),
        ]

    p = Pipeline(steps)
    p.run(inputs)
    
if __name__ == '__main__':
    main()