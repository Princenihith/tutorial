from django.contrib import admin

from .models import Wine, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user']
    search_fields = ['comment']
    
admin.site.register(Wine)
admin.site.register(Review, ReviewAdmin)