from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Instangram.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    
    path("accounts/logout", views.logout_then_login, name= "logout"),
    path('tinymce/', include('tinymce.urls')),
]