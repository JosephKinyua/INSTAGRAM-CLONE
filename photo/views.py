from django.http  import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        likeform = LikeForm(request.POST)
        if commentForm.is_valid():
            pic_id = int(request.POST.get('imageid'))
            pic = Post.objects.get(id=pic_id)
            comment = commentForm.save(commit=False)
            comment.user = request.user
            comment.pic = pic
            comment.save()
    return render(request,'home.html',{'likeform':likeform,'commentForm':commentForm})