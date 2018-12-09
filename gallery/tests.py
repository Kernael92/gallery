from django.test import TestCase
from .models import Image,Location,Category
import datetime as dt 

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
class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new location and saving it
        self.nairobi = Location(name = 'Nairobi')
        self.nairobi.save()

        # Creating a new category and saving it
        self.fashion = Category(name = 'Fashion')
        self.fashion.save()

        self.new_image = Image(image = 'image', image_name = 'image.jpg', image_description = 'a high fashion image taken at the nairobi fashion market event', location = self.nairobi, category = self.fashion)
        self.new_image.save()
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
    def test_get_gallery_today(self):
        today_gallery = Image.todays_gallery()
        self.assertTrue(len(today_gallery) > 0)
    def test_get_gallery_by_date(self):
        test_date = "2018-10-07"
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)
        self.assertTrue(len(gallery_by_date) == 0)


