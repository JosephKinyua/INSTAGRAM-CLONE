
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Profile,Comments
from .forms import CommentForm, LikeForm
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User

@login_required(login_url='accounts/login')
def home(request):
  if request.method == 'POST':
    commentForm = CommentForm(request.POST)
    likeform = LikeForm(request.POST)
    if commentForm.is_valid():
      pic_id = int(request.POST.get('imageid'))
      pic = Post.objects.get(id=pic_id)
      com = commentForm.save(commit=False)
      com.user = request.user
      com.pic = pic
      com.save()
    

      return redirect('/#image'+str(pic_id))

  title = 'this is title'
  allpics = Post.all_pictures()
  commentForm = CommentForm()
  likeform = LikeForm()
  allcomments = Comments.objects.all()
  return render(request, 'home.html', {'title': title, 'allpics':allpics, 'commentForm':commentForm, 'allcomments':allcomments, 'likeform':likeform})