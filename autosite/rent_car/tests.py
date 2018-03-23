from django.test import TestCase
from django.urls import reverse

from .models import Category, MarkAuto, Auto, AutoImage

class RentCarTest(TestCase):
    # models
    def create_category(self, name='Бюджетные авто'):
        return Category.objects.create(name=name)

    def create_mark_auto(self, title='Nissan Almera'):
        return MarkAuto.objects.create(title=title)

    def create_auto(self,
                    year='2015',
                    description='Описание',
                    image='/media/cars/1.img',
                    gears=1,
                    engine=1.5,
                    min_age=19,
                    experience=3,
                    price=1500):
        auto = self.create_mark_auto()
        return Auto.objects.create(
            mark=auto,
            year=year,
            description=description,
            image=image,
            gears=gears,
            engine=engine,
            min_age=min_age,
            experience=experience,
            price=price
        )
    def create_auto_image(self, image='/media/cars/1.img'):
        auto = self.create_auto()
        return AutoImage.objects.create(auto=auto, image=image)

    def test_category_create(self):
        a = self.create_category()

        self.assertTrue(isinstance(a, Category))
        self.assertEqual(a.__str__(), a.name)

    def test_mark_auto_create(self):
        a = self.create_mark_auto()

        self.assertTrue(isinstance(a, MarkAuto))
        self.assertEqual(a.__str__(), a.title)
    def test_auto_create(self):
        a = self.create_auto()
        category1 = a.category.create(name='Бюджетные авто')
        category1.save()

        self.assertTrue(isinstance(a, Auto))
        self.assertEqual(a.__str__(), 'Nissan Almera')
        self.assertEqual(category1.name, 'Бюджетные авто')
        self.assertEqual(a.year, '2015')
        self.assertEqual(a.description, 'Описание')
        self.assertEqual(a.image, '/media/cars/1.img')
        self.assertEqual(a.gears, 1)
        self.assertEqual(a.engine, 1.5)
        self.assertEqual(a.min_age, 19)
        self.assertEqual(a.experience, 3)
        self.assertEqual(a.price, 1500)
    def test_image_create(self):
        a = self.create_auto_image()
        self.assertTrue(isinstance(a, AutoImage))
        self.assertEqual(a.__str__(), 'Nissan Almera')

    # views
    def test_contacts(self):
        url = reverse('contacts')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_developers(self):
        url = reverse('developers')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_category(self):
        a = self.create_category()

        url = reverse('category', args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(reverse('category', args=[a.id]), a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)

    def test_car_info(self):
        a = self.create_auto()

        url = reverse('car_info', args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(reverse('car_info', args=[a.id]), a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
    def test_index(self):
        url = reverse('index')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)