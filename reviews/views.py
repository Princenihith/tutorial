from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Wine 
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    print(latest_review_list)
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)
 
 
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def wine_list(request):
    wine_list = Wine.objects.order_by('-name')
    context = {'wine_list':wine_list}
    return render(request, 'reviews/wine_list.html', context)


def wine_detail(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    form = ReviewForm()
    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})


def add_review(request, wine_id):
    if request.method == 'POST':
        wine = get_object_or_404(Wine, pk=wine_id)
        form = ReviewForm(request.POST)
        print('1')
        if form.is_valid():
            print('2')
            comment = form.save(commit = False)
            comment.user = request.user 
            comment.wine = wine 
                # ***this where i am unable to assign my comment to the respective post***
            #comment.post_id =pk
            comment.save()
            #text1 = form1.cleaned_data['comment']
            #form1 = CommentForm()
            form = ReviewForm()
            return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))
            # args ={
            #         'post':post , 'form1':form1,'comment':comment,
            #         'pk':pk, 'text1': text1,
                     
            #     }
            # return render(request,'home/post_detail.html',args)

        print('3')
        args = {'form': form, }
        return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))    





    # wine = get_object_or_404(Wine, pk=wine_id)
    # form = ReviewForm(request.POST)
    # user_name = request.user
    # print(user_name)
    # if form.is_valid():
    #     rating = form.cleaned_data['rating']
    #     comment = form.cleaned_data['comment']
    #     # user_name = form.cleaned_data['user_name']
    #     user_name = request.user
    #     print(user_name)
    #     if comment:
    #         print(comment)
    #     else:
    #         print('1')
    #     print(rating)
    #     review = Review()
    #     review.wine = wine
    #     review.user_name = user_name
    #     review.rating = rating
    #     review.comment = comment
    #     review.pub_date = datetime.datetime.now()
    #     review.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))

    # return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})




    # def add_review(request, wine_id):
    # wine = get_object_or_404(Wine, pk=wine_id)
    # form = ReviewForm(request.POST)
    # user_name = request.user
    # print(user_name)
    # if form.is_valid():
    #     rating = form.cleaned_data['rating']
    #     comment = form.cleaned_data['comment']
    #     # user_name = form.cleaned_data['user_name']
    #     user_name = request.user
    #     print(user_name)
    #     if comment:
    #         print(comment)
    #     else:
    #         print('1')
    #     print(rating)
    #     review = Review()
    #     review.wine = wine
    #     review.user_name = user_name
    #     review.rating = rating
    #     review.comment = comment
    #     review.pub_date = datetime.datetime.now()
    #     review.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('reviews:wine_detail', args=(wine.id,)))

    # return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})