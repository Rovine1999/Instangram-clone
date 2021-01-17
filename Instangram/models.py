from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    # form.instance.user = Profile.objects.get(user=self.request.user)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('image')
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    
    @classmethod
    def get_profile(request, id):
        try:
            profile = Profile.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return profile
        
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.bio 


class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    
    
    
class Comment(models.Model):
    comment = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE )
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
