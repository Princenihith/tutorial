from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    post = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'profile_image')
    user = models.ForeignKey(User ,on_delete = 'models.CASCADE')
    likes = models.ManyToManyField(User , related_name='likes', blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    restrict_comment =  models.BooleanField(default=False)

    def __str__(self):
        return self.post

    def total_likes(self):
        return self.likes.count()
 
    def get_absolute_url(self,request):
        # id = request.POST.get('post_id')
        return reverse('home:Post_detail',kwargs={'pk':post_id})


class ImagePost(models.Model):
	user = models.ForeignKey(User ,on_delete = 'models.CASCADE')
	post = models.CharField(max_length= 500)
	image =  models.FileField(upload_to = 'profile_image')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = 'models.CASCADE')
    post = models.ForeignKey(Post, null = True, on_delete = 'models.CASCADE')
    reply = models.ForeignKey('self',null=True,related_name= 'replies',on_delete='models.CASCADE')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

 
    def __str__(self):
        return self.comment
        
