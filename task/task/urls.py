from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from task import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^home/', views.home, name='home'),
    url(r'^', views.home, name='social_auth')
]
