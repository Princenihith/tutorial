from django import forms
from home.models import Post, ImagePost,Comment


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('post','image',)

class Home(forms.ModelForm):
	post = forms.CharField()
	image = forms.FileField()
	

	class Meta:
		model = ImagePost
		fields = ('post' , 'image' ,)

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)