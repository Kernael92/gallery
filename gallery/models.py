from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.name 
    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.name 
    def save_category(self):
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['image']

    def save_image(self):
        self.save()
    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(pub_date__date = today)
        return gallery
    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(pub_date__date = date)
        return gallery
    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__icontains=search_term)
        return gallery
    @classmethod
    def get_image(cls,image_id):
        image = cls.objects.get(id = image_id)
        return image





