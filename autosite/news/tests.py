from django.test import TestCase
from django.urls import reverse

from .models import News

from .views import show_news, get_news

class NewsTest(TestCase):
    def create_tiding(self, title='test tiding', text='test text', image='test_img'):
        return News.objects.create(
            title=title,
            text=text,
            image=image,
            )

    def test_tiding_creation(self):
        a = self.create_tiding()

        self.assertTrue(isinstance(a, News))
        self.assertEqual(a.__str__(), a.title)

    def test_get_news(self):
        a = self.create_tiding()
        url = reverse('get_news')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    
    def test_show_news(self): 
        a = self.create_tiding()
        url =  reverse('show_news', args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(reverse('show_news', args=[a.id]), a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)