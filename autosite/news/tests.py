from django.test import TestCase

from .models import News


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