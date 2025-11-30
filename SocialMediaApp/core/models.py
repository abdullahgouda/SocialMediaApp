from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    profile_picture = models.ImageField(default="profile_pics/default.jpg", upload_to="profile_pics")
    bio = models.TextField(max_length=500, blank=True , null=True , default="")

    def get_num_posts(self):
        return Post.objects.filter(user=self).count()
    
    def is_following(self , user_B):
        count = Friend.objects.filter(user_A = self , user_B = user_B).count()

        if count > 0:
            return True
        else:
            return False
    
    def get_following(self):
        following = Friend.objects.filter(user_A = self)
        temp = []
        for item in following:
            temp.append(item.user_B.id)
        return temp

class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=False)
    caption = models.TextField(max_length=600 , null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    
class Friend(models.Model):

    user_A = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_A')
    user_B = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_B')

    def __str__(self):
        return self.user_A.username + '====' + self.user_B.username
    