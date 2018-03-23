from django.test import TestCase
from .models import Order



class OrdersTest(TestCase):
    def create_order(self,
                     car='Lada Kalina',
                     name='Вася',
                     phone='89123112313',
                     deadline='1 день',
                     status=False):
         return Order.objects.create(
                     car=car,
                     name=name,
                     phone=phone,
                     deadline=deadline,
                     status=status,
                 )


    def test_order_create(self):
        a = self.create_order()

        self.assertTrue(isinstance(a, Order))
        self.assertEqual(a.__str__(), '{}, {}'.format(a.car, a.phone))