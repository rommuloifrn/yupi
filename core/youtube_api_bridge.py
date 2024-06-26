import requests, re
from django.conf import settings

class Parser:
    def parse_url(url):
        pattern = '^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*' #'^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*'
        video_id = re.search(pattern, url).group(2)
        
        return video_id

class APIHandler:
    key = settings.API_KEY
    url = 'https://www.googleapis.com/youtube/v3/videos?'
    
    @staticmethod
    def get_video_info(video_id): # https://developers.google.com/youtube/v3/docs/videos/list
        url = APIHandler.url
        key = APIHandler.key
        
        response = requests.get(f'{url}&id={video_id}&key={key}&part=snippet&fields=items/snippet/title,items/snippet/thumbnails')
        
        print(f"debug: {response.json()}, {response.status_code}")
        items = response.json()['items']
        
        # for some reason the API returns 200 even when it doesnt find the video i requested.
        if len(items)>0:
            return items[0]['snippet']
        else: 
            return None
        