from django.db import models
from django.db.models.signals import post_save	
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

# class Username(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	# username = models.CharField(label='Enter Username', min_length=4, max_length=150)
# 	email = models.EmailField(label='Enter email')
# 	password1 = models.CharField(label='Enter password', widget=forms.PasswordInput)
# 	password2 = models.CharField(label='Confirm password', widget=forms.PasswordInput)
# 	radio = models.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
 


class UserProfileManager(models.Manager):
	"""docstring for UserProfileManager"""
	def get_queryset(self):
		super(UserProfileManager, self).get_queryset().filter(city = 'london')
		

class UserProfile(AbstractBaseUser):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	image = models.ImageField(upload_to = 'profile_img',blank= True)
    
	USERNAME_FIELD = 'user'

	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.user

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile , sender = User)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to = 'image', null=True, blank=True)


    def __str__(self):
        return "Profile of user {}".format(self.user.username)

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.name