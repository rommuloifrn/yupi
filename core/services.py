from .models import VideoUnit, Pin, VideoUnit
from django.conf import settings
import requests
from datetime import datetime, timedelta

class YoutubeAPIService():
    key = settings.API_KEY
    url = 'https://www.googleapis.com/youtube/v3/videos?'
    
    @staticmethod
    def get_video_info(video_id): # https://developers.google.com/youtube/v3/docs/videos/list
        url = YoutubeAPIService.url
        key = YoutubeAPIService.key
        
        response = requests.get(f'{url}&id={video_id}&key={key}&part=snippet, contentDetails&fields=items/snippet/title, items/snippet/thumbnails, items/contentDetails/duration, items/snippet/publishedAt')
        
        print(f"debug: {response.json()}, {response.status_code}, id:{video_id}")
        items = response.json()['items']
        
        print(f"debug: {items}")
        
        # for some reason the API returns 200 even when it doesnt find the video i requested.
        if len(items)>0:
            items = items[0]
            #snippet = resource[0]['snippet']
            #content_details = resource[0]['contentDetails']
            #return items
            duration_raw = items['contentDetails']['duration']
            duration_proc = duration_raw.replace('PT', '').replace('M', ':').replace('H', ':').replace('S', '')
            try: dt = datetime.strptime(duration_proc, '%H:%M:%S')
            except: dt = datetime.strptime(duration_proc, '%M:%S')
            
            delta = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
            return VideoUnit(youtube_id=video_id, title=items['snippet']['title'], duration=delta, published_at=items['snippet']['publishedAt'], thumbnail_url=items['snippet']['thumbnails']['medium']['url'])
        
        else:
            return None


    
    
class YoutubeVideoService():
    def create(video_id):
        video_resource = YoutubeAPIService.get_video_info(video_id)
        if video_resource == None:
            return None
        video = video_resource #VideoUnit(video_id, video_resource.items.snippet.title, video_resource.contentDetails.duration, video_resource.snippet.published_at, video_resource.thumbnails.medium)
        video.save()
        return video

    def get_or_create(identifierr):
        try:
            video = VideoUnit.objects.get(youtube_id=identifierr)
        except VideoUnit.DoesNotExist:
            video = YoutubeVideoService.create(identifierr)
        return video

        
        
class PinService():
    def create_pin(request, pin, video_id):
        video = YoutubeVideoService.get_or_create(video_id)
        if video == None:
            raise Exception("resource not encountered.")
        pin.video = video
        pin.save()