from django.test import TestCase

from .models import Category, MarkAuto, Auto, AutoImage

class RentCarTest(TestCase):
    def create_category(self, name='Бюджетные авто'):
        return Category.objects.create(name=name)

    def create_mark_auto(self, title='Nissan Almera'):
        return MarkAuto.objects.create(title=title)

    def test_category_create(self):
        a = self.create_category()

        self.assertTrue(isinstance(a, Category))
        self.assertEqual(a.__str__(), a.name)

    def test_mark_auto_create(self):
        a = self.create_mark_auto()

        self.assertTrue(isinstance(a, MarkAuto))
        self.assertEqual(a.__str__(), a.title)

    

    