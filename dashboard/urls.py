"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cart.views.home', name='home'),
    url(r'^login/$', 'cart.views.login_page', name='login_page'),
    url(r'^logout/$', 'cart.views.logout_page', name='logout_page'),
    url(r'^accounts/logout/$', 'cart.views.logout_page', name='logout_page'),
    url(r'^accounts/login/$', 'cart.views.login_page', name='login_page'),

    # 'registration.views.registration_form' view
    url(r'register/$', 'registration.views.registration_form'),
      
    # Allow the URLs beginning with /captcha/ to be handled by
    # the urls.py of captcha module from 'django-simple-captcha'
    url(r'^captcha/', include('captcha.urls')),
]
