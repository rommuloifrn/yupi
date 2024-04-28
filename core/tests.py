from django.test import TestCase
from .services import YoutubeAPIService

# Create your tests here.

class YoutubeTestCase(TestCase):
    def test_consume(self):
        video_reg = YoutubeAPIService.get_video_info('OipEz8mJfeQ')
        self.assertEqual('Midnight Express', video_reg.title)