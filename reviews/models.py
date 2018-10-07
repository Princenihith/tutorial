from django.db import models
from accounts.models import User
import numpy as np


class Wine(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'product_image', null=True, blank=True)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name
    def __str__(self):
    	return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete = 'models.CASCADE')
    wine = models.ForeignKey(Wine, on_delete = 'models.CASCADE')
    pub_date = models.DateTimeField(auto_now_add=True)
    # user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __unicode__(self):
        return self.wine.name
    def __str__(self):
        return self.wine.name