from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile,UserProfile
						# ,Username
from django.core.exceptions import ValidationError

CHOICES = [('1', 'PROFESSIONAL',), ('0', 'USER',)]

# class UsernameForm(models.ModelForm):
# 	class meta:
# 		model = Username
# 		fields = ('user','username','email','password1','password2','radio')



# class CustomUserCreationForm(forms.ModelForm):
#     username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
#     email = forms.EmailField(label='Enter email')
#     password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#     radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = User.objects.filter(username=username)
#         if r.count():
#             raise  ValidationError("Username already exists")
#         return username

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         r = User.objects.filter(email=email)
#         if r.count():
#             raise  ValidationError("Email already exists")
#         return email

#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Password don't match")

#         return password2

#     def save(self, commit=True):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             email = self.cleaned_data['email'],
#             password = self.cleaned_data['password1'],
#             radio = self.cleaned_data['radio']
#         )
#         return user



# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','radio' )


class RegistrationForm(forms.ModelForm):
	radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
	confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
	class Meta:
		model = User
		fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

	def clean_confirm_password(self):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError("Password Mismatch")
		return confirm_password









# class RegistrationForm(UserCreationForm):
# 	email = forms.EmailField(required = True)
# 	radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

# 	class Meta:
# 		model = User
# 		fields = (
# 		     'username',
# 		     'first_name',
# 		     'last_name',
# 		     'email',
# 		     'password1',
# 		     'password2',
# 		     'radio',
# 		)	
# 	def save(self, commit = True):
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.first_name = self.cleaned_data['first_name']
# 		user.last_name = self.cleaned_data['last_name']
# 		user.email = self.cleaned_data['email']
# 		user.radio = ['radio']

# 		if commit:
# 			user.save()

# 			return user


class EditProfileForm(UserChangeForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				]

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ('user',)

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        exclude=[
        	'Password',
        	'last_login',
        ]
        def clean_password(self):
        	return self.initial["password"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user',
        			'password',
        			'last_login',
        			]
 



# class UserEditForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         )

# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user',)






# class EditProfileForm(UserChangeForm):

# 	class Meta:
# 		model = User
# 		fields = {
# 			'first_name',
# 			'last_name',
# 			'email',
# 			'password',	
# 		}
# 		exclude= ('password',)

# 		def clean_password(self):
# 			 return self.initial["password"]

# class modelform(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ['description', 'city' , 'website',
# 				'phone', 'image']



# 	def save(self, commit = True):
# 		UserProfile = super(modelform, self).save(commit=False)
# 		UserProfile.description = self.cleaned_data['description']
# 		UserProfile.city = self.cleaned_data['city']
# 		UserProfile.website = self.cleaned_data['website']
# 		UserProfile.phone = self.cleaned_data['phone']
# 		UserProfile.image = self.cleaned_data['image']

# 		if commit:
# 			UserProfile.save()

# 			return UserProfile


