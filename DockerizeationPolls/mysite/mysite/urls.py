"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#import sys
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from polls import urls

# p8 - link to setub debug tool -> step 7
#if not settings.TESTING:
#    urlpatterns = [
#        *urlpatterns,
#    ] + debug_toolbar_urls()

urlpatterns = [
    path("polls/", include("polls.urls")), #imports our polls.url path from polls/view.py
    path('admin/', admin.site.urls)
] + debug_toolbar_urls()

# Cross-Origin request blocked (debug tool)
# may read as :"Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://localhost/static/debug_toolbar/js/toolbar.js. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing)."
# or :"Access to script at 'http://localhost/static/debug_toolbar/js/toolbar.js' from origin 'http://localhost:8000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource."
# RESOLVE: configure your static file server to ass the 'Access-Control-Allow-Origin header' with the origin of the application server.
# EX) application server is at http://example.com, and your static files are served by:
# NGINX, add:
# add_header Access-Control-Allow-Origin http://example.com;

# And for Apache:
# Header add Access-Control-Allow-Origin http://example.com

#see under step 7, Troubleshooting in: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
