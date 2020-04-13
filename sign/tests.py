from django.test import TestCase
from sign.models import Event, Guest

# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", limit=2000, statue=True,

                                    address='shenzhen', start_time='2018-12-20 08:47:59')
        Guest.objects.create(id=1, real_name='王芳',
                                phone='15900001234', email='wangfang@mail.com', sign=False,  event_id=1,)

    def test_event_models(self):
            result = Event.objects.get(name="oneplus 3 event")
            self.assertEqual(result.address, "shenzhen")
            self.assertEqual(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='15900001234')
        self.assertEqual(result.real_name, "王芳")
        self.assertEqual(result.sign)


