from django.db import models


# Create your models here.
class Location(models.Model):

    '''
    locations model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
       return self.location
       
    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()

class Category(models.Model):

    '''
    Photo category model
    '''
    
    name = models.CharField(max_length=120)

    def __str__(self):
       return self.name
    
    def save_category(self):
        self.save()

    

class Image(models.Model):

    '''
    Images model
    '''
    
    image = models.ImageField(upload_to='gallery/', blank=True)
    image_url = models.TextField(blank=False)
    image_name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location)

    def __str__(self):
       return self.image_name