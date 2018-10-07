from django.views.generic import TemplateView
from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User
from home.forms import HomeForm,Home,CommentForm
from home.models import Post ,ImagePost,Comment
from django.db.models import Q
from django.urls import reverse 
from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import render_to_string

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        post_list = None
        form = HomeForm(self.request.GET or None)
        form1 = CommentForm(self.request.GET or None)
        posts = Post.objects.filter(user = request.user).order_by('-created')
        comments = Comment.objects.all()
        users = User.objects.exclude(id=request.user.id)
        query = request.GET.get('q')    
        if query:
                posts = Post.objects.filter(
                        Q(post__icontains=query)
                        )
                context = {
                        'posts': posts, }   
                print(posts)
        args = {
            'form': form, 'posts': posts, 'users': users, 'form1':form1,
            'comments':comments,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form1 = CommentForm()
        text = ''
        # if request.method == 'POST':
        #     form = HomeForm(request.POST,request.FILES)
        #     if form.is_valid():

        #         post = form.save(commit=False)
        #         post.user = request.user
        #         post.save()
        #         text = form.cleaned_data['post']
        #         form = HomeForm()
        #         form1 = CommentForm()
        #         return redirect('home:home')
        if request.method=='POST' and 'btn1' in request.POST:
            post_list = Post.published.all()
            query = request.GET.get('q')
            if query:
                post_list = Post.objects.filter(
                        Q(post__icontains=query)
                        )
                context = {
                        'posts_list': posts_list,
                                }
                print(posts_list)
                return redirect('home:home')
        if request.method=='POST' and 'btn' in request.POST:
            form = HomeForm(request.POST,request.FILES)
            if form.is_valid():

                post = form.save(commit=False)
                post.user = request.user
                post.save()
                text = form.cleaned_data['post']
                form = HomeForm()
                form1 = CommentForm()
        return redirect('home:home')


# def post_list(request):
#     post_list=None
#     query = request.GET.get('q')
#     if query:
#         post_list = Post.published.filter(
#                 Q(post__icontains=query)|
#                 Q(author__username=query)
#                 )  
#     context = {
#         'post_list': post_list,

#     }
        # if request.method == 'POST':
        #     form1 = CommentForm(request.POST,Post.id)
        #     text1 = ''
        #     post = ''
        #     if form1.is_valid():
        #         comment = form1.save(commit = False)
        #         comment.user = request.user  
        #         # ***this where i am unable to assign my comment to the respective post***
        #         # comment.post_id =post.id
        #         comment.save()
        #         text1 = form1.cleaned_data['comment']
        #         form1 = CommentForm()
        #         form = HomeForm()
        #         return redirect('home:home')


        # args = {'form': form, 'text': text ,'text1': text1 , 'form1':form1}
        # return render(request, self.template_name, args)


def Post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk,reply = None).order_by('-pk')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    form1 = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        reply_id = None
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form= CommentForm()

    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('home/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'home/post_detail.html', context)


# class LikeView(TemplateView):
#     template_name = 'home/post_detail.html'

#     def post(self,request):
#         post = get_object_or_404(Post,id = request.POST.get('post_id'))
#         post.likes.add(request.user)
#         return HttpResponseRedirect(Post.get_absolute_url(self))

#     def get_absolute_url(self,request):
#         id = request.POST.get('post_id')
#         return reverse('home:Post_detail',kwargs={'pk':id})


def like_post(request):
    # post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),

    }
    if request.is_ajax():
        html = render_to_string('home/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    
    



def cmnt(request,pk):
    if request.method == 'POST':
        form = HomeForm()
        form1 = CommentForm(request.POST or None)
        text1 = '' 
        post = ''
        if form1.is_valid():
            comment = form1.save(commit = False)
            comment.user = request.user  
                # ***this where i am unable to assign my comment to the respective post***
            comment.post_id =pk
            comment.save()
            text1 = form1.cleaned_data['comment']
            form1 = CommentForm()
            form = HomeForm()
            return HttpResponseRedirect(get_absolute_url())
            # args ={
            #         'post':post , 'form1':form1,'comment':comment,
            #         'pk':pk, 'text1': text1,
                     
            #     }
            # return render(request,'home/post_detail.html',args)


        args = {'form': form, 'text1': text1 , 'form1':form1}
        return render(request, 'home/home.html', args)










# def like_post(request):
#         post = get_object_or_404(Post,id=request.POST.get("post_id"))
#         is_liked = False
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#             is_liked = False
#         else:
#             is_liked = True
#             post.likes.add(request.user.id)
#         return HttpResponseRedirect(post.get_absolute_url())
    





















# class HomeView(TemplateView):
#     template_name = 'home/home.html'

#     def get(self, request):
#         form = HomeForm()
#         form1 = CommentForm()
#         posts = Post.objects.filter(user = request.user).order_by('-created')
#         comments = Comment.objects.all()
#         users = User.objects.exclude(id=request.user.id)
#         args = {
#             'form': form, 'posts': posts, 'users': users, 'form1':form1,
#             'comments':comments,
#         }
#         return render(request, self.template_name, args)

#     def post(self, request):
#         form1 = CommentForm()
#         text = ''
#         if request.method == 'POST':
#             form = HomeForm(request.POST,request.FILES)
#             if form.is_valid():
                
#                 post = form.save(commit=False)
#                 post.user = request.user
#                 post.save()
#                 text = form.cleaned_data['post']
#                 form = HomeForm()
#                 form1 = CommentForm()
#                 return redirect('home:home')
                
#         def cmnt(self , request):
#             text = ''
#             form1 = CommentForm()
#             if request.method == 'POST':
#                 form1 = CommentForm(request.POST,post.id)
#                 if form.is_valid():
#                     comment = form.save(commit = False)
#                     comment.user = request.user
#                     comment.post = request.post
#                     comment.save()
#                     text = form.cleaned_data['comment']
#                     form1 = CommentForm()
#                     form = HomeForm()
#                     return redirect('home:home')

#                 args = {'form': form, 'text': text , 'form1':form1}
#                 return render(request, self.template_name, args)


  



    

