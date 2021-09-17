from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('home',views.home,name = 'home'),
    path('', views.profile, name='uprofile'),
    path('postpic', views.post_pic, name='postpic'),
    path('imagedetails/<int:id>', views.imagedetails, name='imagedetails'),
    path('userprofile/<int:id>', views.userprofile, name='userprofile'),
    path('search/', views.searchUser, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)