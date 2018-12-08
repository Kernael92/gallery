from django.db import models

# Create your models here.

class Location(models.Model):
    name =models.CharField(max_length = 100)

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 245)

    def __str__(self):
        return self.name 


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
    class Meta:
        ordering = ['image']





