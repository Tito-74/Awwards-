from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pict = CloudinaryField('images')
    bio = models.TextField(max_length = 250, blank=True)
    name = models.CharField(max_length = 50, blank=True)
    phone = models.CharField(max_length = 15, blank=True)
    country = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

   

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length = 100)
    project_image = CloudinaryField('images')
    desc = models.TextField(max_length = 250)
    url_link = models.URLField(max_length = 254, blank = True)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def post_by_id(cls, id):
        project = Project.objects.filter(id=id)
        return project

    @classmethod
    def search_post(cls, name):
        return cls.objects.filter(title__icontains=name).all()





class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null = True)
    design = models.IntegerField(default = 0, blank = False)
    usability = models.IntegerField(default = 0, blank = False)
    creativity = models.IntegerField(default = 0, blank = False)
    comment = models.TextField(max_length = 250)
    date_rated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.post.title


