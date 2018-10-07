




from django.shortcuts import render , redirect
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from accounts.forms import RegistrationForm, EditProfileForm,ProfileEditForm,UserEditForm
							# modelform ,CustomUserCreationForm,SignUpForm,UsernameForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import Profile, UserProfile
									# ,Username
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from .import forms
from django.db.models import Q
from home.models import Post 
# Create your views here.

def signup(request,radio):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/reg_form.html', {'form': form})








# def register(request):
# 	if request.method == 'POST':
# 		form = RegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect(reverse('accounts:login'))
# 	else:
# 		form = RegistrationForm()

# 	args = {'form':form}
# 	return render(request, 'accounts/reg_form.html',args)

# def view_profile(request, pk=None):
#     if pk:
#         print(pk)
#         print('1')
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#         print('2')
#     args = {'user': user}
#     return render(request, 'accounts/profile.html', args)
# @login_required
# def view_profile(request, username):
#     if username:
#         #print(pk)
#         print('1')
#         user = User.objects.get(username=username)
#     else:
#         print('2')
#         user = request.user
#     args = {'user': user}
#     return render(request, 'accounts/profile.html', args)


# @login_required
# def edit_profile(request, username):
#     if username:
#         if request.method == 'POST':
#             #user_form = EditProfileForm(data=request.POST or None, instance=request.user)
#             profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.userprofile, files=request.FILES)
#             if profile_form.is_valid():
#                 print(profile_form)
#                 #user_form.save()
#                 profile_form.save()
#                 return HttpResponseRedirect(reverse("accounts:edit_profile"))
#         else:
#             #user_form = EditProfileForm(instance=request.user)
#             profile_form = ProfileEditForm(instance=request.user.userprofile)
#     else:
#         #user_form = EditProfileForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.userprofile)

#     context = {
#         #'user_form': user_form,
#         'profile_form': profile_form,
#     }
#     return render(request, 'accounts/edit_profile.html', context)

def view_profile(request, username=None):
    if username:
        #print(pk)
        print(username)
        user = User.objects.get(username=username)
        #user = get_object_or_404(User, username=username)
    else:
        print('NO USERNAME')
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print('3')
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.userprofile, files=request.FILES)
        if profile_form.is_valid():
            print('1')
            if user_form.is_valid():
                print('4')
                #print(profile_form)
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect(reverse("accounts:edit_profile"))
            else:
                print('6')
        else:
            print('5')
    else:
        print('2')
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/edit_profile.html', context)





def view_model(request,pk=None):
    if pk:
        user = user.UserProfile.objects.get(pk=pk)
    else:
        user = request.user.UserProfile
    args = {'user': user}
    return render(request, 'accounts/profile_model.html', args)

# def edit_profile(request):
# 	if request.method == 'POST':
# 		form = EditProfileForm(request.POST, instance=request.user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect(reverse('accounts:profile'))
# 	else:
# 		form = EditProfileForm(instance = request.user)
# 		args = {'form': form}
# 		return render(request, 'accounts/edit_profile.html', args)










def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect(reverse('accounts:profile'))
		else:
			return redirect(reverse('accounts:change_password'))
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
def model(request):
	if request.method == 'POST':
		form = modelform(data = request.POST , instance = request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:profile'))
		else:
			return redirect(reverse('accounts:model'))
	else:
		form = modelform(instance = request.user)
		args = {'form' : form}
		return render(request , 'accounts/model.html',args)















	# return render(request, 'accounts/model.html', {'form':form})

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			UserProfile.objects.create(user=new_user)
			return redirect(reverse('accounts:login'))
	else:
		form = RegistrationForm()
	context = {
        'form': form,
    }
	return render(request, 'accounts/reg_form.html', context)


# class HomeView(TemplateView):
#     template_name = 'home/home.html'

#     def get(self, request):
#         post_list = None
#         form = HomeForm(self.request.GET or None)
#         form1 = CommentForm(self.request.GET or None)
#         posts = Post.objects.filter(user = request.user).order_by('-created')
#         comments = Comment.objects.all()
#         users = User.objects.exclude(id=request.user.id)
#         query = request.GET.get('q')    
#         if query:
#                 posts = Post.objects.filter(
#                         Q(post__icontains=query)
#                         )
#                 context = {
#                         'posts': posts, }   
#                 print(posts)
#         args = {
#             'form': form, 'posts': posts, 'users': users, 'form1':form1,
#             'comments':comments,
#         }
#         return render(request, self.template_name, args)

#     def post(self, request):
#         form1 = CommentForm()
#         text = ''
#         # if request.method == 'POST':
#         #     form = HomeForm(request.POST,request.FILES)
#         #     if form.is_valid():

#         #         post = form.save(commit=False)
#         #         post.user = request.user
#         #         post.save()
#         #         text = form.cleaned_data['post']
#         #         form = HomeForm()
#         #         form1 = CommentForm()
#         #         return redirect('home:home')
#         if request.method=='POST' and 'btn1' in request.POST:
#             post_list = Post.published.all()
#             query = request.GET.get('q')
#             if query:
#                 post_list = Post.objects.filter(
#                         Q(post__icontains=query)
#                         )
#                 context = {
#                         'posts_list': posts_list,
#                                 }
#                 print(posts_list)
#                 return redirect('home:home')
#         if request.method=='POST' and 'btn' in request.POST:
#             form = HomeForm(request.POST,request.FILES)
#             if form.is_valid():

#                 post = form.save(commit=False)
#                 post.user = request.user
#                 post.save()
#                 text = form.cleaned_data['post']
#                 form = HomeForm()
#                 form1 = CommentForm()
#         return redirect('home:home')

def search(request):
    template_name = 'accounts/search.html'
    results = None
    name = None
    post =None
    product = None
    print("1")
    query = request.GET.get('q')
    a = request.GET.get('cars')
    print(a)
    print(query)
    if query:
        if a == '1':
            print("1")
            name = User.objects.filter(Q(username__icontains=query))
            print(name)
        else:
            if a=='2':
                product = Post.objects.filter(Q(post__icontains=query))
                print(product)
            else:
                if a=='3':
                    post = Post.objects.filter(Q(post__icontains=query))
                    print(post)
        # def switch(a):
        #     switcher={
        #                 1: lambda name : User.objects.filter(
        #                                          Q(username__icontains=query)
        #                                         ),
        #                 2: lambda name : Post.objects.filter(
        #                                          Q(post__icontains=query)
        #                                         ),
        #                 3: lambda name : Post.objects.filter(
        #                                          Q(product__icontains=query)
        #                                          ),
        #             }
    else:
        results = Post.objects.all().order_by('-created')



    context = {
                'po': post,'n': name, 'p':product,
                're': results,
    }
    return render(request, template_name, context)

# def search(request):
#     if request.method== 'GET':
#         query=request.GET.get('q')
#         a = request.GET.get('cars')
#         print(query)
#         print(a)
#         if query:
#             results = Post.objects.filter(Q(post__icontains=query))

#             if results:
#                 return render(request, 'accounts/search.html', {'results': results})
#             else:
#                 messages.error(request, 'no result found')
#         else:
#             return HttpResponseRedirect('accounts/search.html')
#     return render(request, 'accounts/search.html')

# def search(request):
#     template_name = 'accounts/search.html'
#     results = None
#     query = request.GET.get('q')
#     a = request.GET.get('cars')
#     print(a)
#     print(query)
#     if query:
#         # def switch(a):
#         #      switcher={
#         #             hairdresser: results = Post.objects.filter(
#         #                                     Q(title__icontains=query)
#         #                                     )
#         #             post: results = Post.objects.filter(
#         #                                     Q(post__icontains=query)
#         #                                     )
#         #             product: results = Post.objects.filter(
#         #                                     Q(product__icontains=query)
#         #                                     )
#         #             }
#         # if(a == 1):
#             results = User.objects.filter(Q(username__icontains=query))
#             print(results)
#         # elif (a==2):
#         #     results = Post.objects.filter(Q(product__icontains=query))
#         #     print(results)
#         # elif (a==3):
#         #     results = Post.objects.filter(Q(post__icontains=query))
#         #     print(results)
#     else:
#         results = Post.objects.all().order_by('-created')



#     context = {
#                 'r': results,
#     }
#     return render(request, template_name, context)           
        