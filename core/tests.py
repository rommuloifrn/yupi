from django.test import TestCase
from .services import YoutubeAPIService

# Create your tests here.

class YoutubeTestCase(TestCase):
    
    
    def test_if_can_retrieve_resource_title(self):
        video_unit = YoutubeAPIService.get_video_as_video_unit('OipEz8mJfeQ')
        self.assertEqual('Midnight Express', video_unit.title)
        
    def test_if_get_none_when_resource_is_not_found(self):
        video_unit = YoutubeAPIService.get_video_as_video_unit(')()()())')
        self.assertEqual(None, video_unit)