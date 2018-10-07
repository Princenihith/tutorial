from django.contrib import admin
from accounts.models import UserProfile 
from home.models import Post
from accounts.models import Profile,Product
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info','phone','image')
	list_filter = ('phone', 'image')
	search_fields = ('description',)
	ordering = ('phone','user','image')


	def user_info(self , obj):
		return obj.user

	def query_set(self , request):
		queryset = queryset.objects.order_by('phone')

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)


