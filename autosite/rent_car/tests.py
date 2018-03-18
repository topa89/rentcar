from django.test import TestCase

from .models import Category, MarkAuto, Auto, AutoImage

class RentCarTest(TestCase):
    # models
    def create_category(self, name='Бюджетные авто'):
        return Category.objects.create(name=name)

    def create_mark_auto(self, title='Nissan Almera'):
        return MarkAuto.objects.create(title=title)

    #def create_auto(self, year = '2015',
     #    description='Описание', image='/media/cars/1.img', gears=1, engine=1.5, min_age=19, experience=3, price=1500):
      #  a = self.create_category()
       # return Auto.objects.create(mark=self.create_mark_auto(), category = a.groups.all(), year=year, description=description, image=image, gears=gears,
        #engine=engine, min_age=min_age, experience=experience, price=price)

    def test_category_create(self):
        a = self.create_category()

        self.assertTrue(isinstance(a, Category))
        self.assertEqual(a.__str__(), a.name)

    def test_mark_auto_create(self):
        a = self.create_mark_auto()

        self.assertTrue(isinstance(a, MarkAuto))
        self.assertEqual(a.__str__(), a.title)
    

    # views

    