from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClasss(TestCase):

    # set up method
    def setUp(self):
        self.nairobi = Location(name = 'Nairobi')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))
    # Testing the save method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)


class CategoryTestClass(TestCase):
    # set up method
    def setUp(self):
        self.fashion = Category(name = 'Fashion')
    # testing instace
    def test_instance(self):
        self.assertTrue(isinstance(self.fashion,Category))
     # Testing the save method
    def test_save_method(self):
        self.fashion.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


