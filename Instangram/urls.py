from django.urls import path,re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name = 'newsToday'),
    path('search/', views.search_results, name='search_results'),
    path('comment/', views.comment, name='comment'),
    path('post/', views.post, name='post'),
    path('accounts/profile/', views.profile, name='profile'),
    path('image/(\d+)', views.get_image, name='image_results'),
    path('like/<int:pk>/', views.like_image, name='like_post'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
