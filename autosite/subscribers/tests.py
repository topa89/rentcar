from django.test import TestCase

from .models import Subscribers
from .forms import SubscriberForm

class SubscriberTests(TestCase):
    # models
    @classmethod
    def create_subscribers(self, email = 'er@ya.com'):
        return Subscribers.objects.create(email = email)
    
    def test_create_subscribers(self):
        a = self.create_subscribers()

        self.assertTrue(isinstance(a, Subscribers))
        self.assertEqual(a.__str__(), a.email)

    # views
    def test_form(self):
        form_data = {'email': 'example@mail.com'}
        form = SubscriberForm(data=form_data)

        self.assertTrue(form.is_valid())
