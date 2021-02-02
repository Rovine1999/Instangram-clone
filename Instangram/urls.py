
from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name = 'index'),
    path('search/', views.search_results, name='search_results'),
    path('new/comment/', views.comment, name='comment'),
    path('new/post/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('image/(\d+)', views.get_image, name='image_results'),
    path('like/<int:pk>/', views.like_image, name='like_post'),
    path('registration/', views.registerPage, name="registration"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)