import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import VideoUnit, Pin, VideoUnit
from datetime import datetime, timedelta
from isoduration import parse_duration


class YoutubeAPIService():
    key = settings.API_KEY
    url = 'https://www.googleapis.com/youtube/v3/videos?'
    
    @staticmethod
    def get_video_as_video_unit(video_id): # https://developers.google.com/youtube/v3/docs/videos/list
        url = YoutubeAPIService.url
        key = YoutubeAPIService.key
        
        response = requests.get(f'{url}&id={video_id}&key={key}&part=snippet, contentDetails&fields=items/snippet/title, items/snippet/thumbnails, items/contentDetails/duration, items/snippet/publishedAt')
        json = response.json()
        videoresource = json['items']
        print(f"debug: {response.json()}, status code: {response.status_code}, video id:{video_id}")
        if not videoresource: # video not found
            return None
        else:
            data = videoresource[0]
        
            duration = parse_duration(data['contentDetails']['duration'])
            delta = timedelta(days=int(duration.date.days), hours=int(duration.time.hours), minutes=int(duration.time.minutes), seconds=int(duration.time.seconds))
            
            return VideoUnit(youtube_id=video_id, title=data['snippet']['title'], duration=delta, published_at=data['snippet']['publishedAt'], thumbnail_url=data['snippet']['thumbnails']['medium']['url'])
        

    
class YoutubeVideoService():
    def create(video_id):
        video_resource = YoutubeAPIService.get_video_as_video_unit(video_id)
        if video_resource == None:
            return None
        video = video_resource
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
        # acho que esse método deve chamar outro método pra checar se o id de vídeo é válido.
        video = YoutubeVideoService.get_or_create(video_id)
        if video == None:
            raise Exception("resource not encountered.")
        pin.video = video
        pin.save()
        
    def is_owner(user, pin):
        if pin.user != user:
            raise Exception("You shouldn't touch that!")
        return True
    
    def update_pin(request, pin):
        if PinService.is_owner(request.user, pin):
            pin.save()
    
    def delete_pin(request, pin_id):
        pin = get_object_or_404(Pin, pk=pin_id)
        if PinService.is_owner(request.user, pin):
            pin.delete()