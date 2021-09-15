
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Profile,Comments
from .forms import UserForm, ProfileForm,CommentForm, LikeForm
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
@login_required(login_url='accounts/login')
def profile(request):
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,('Your profile was successfully updated!'))
    return redirect('uprofile')

  title = 'Profile'
  user_form = UserForm(instance=request.user)
  profile_form = ProfileForm(instance=request.user)
  user_pics = Post.user_pictures(request.user.username)
  return render(request, 'profile/home.html', {'title':title, "user":request.user, "user_form":user_form, 'profile_form':profile_form, 'user_pics':user_pics})
