"""socialapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
#from django.conf.url.static import static
from socialbot.views import sign_up, log_in, feed_view, post_view, like_view, comment_view,log_out,contact_us

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',log_in),
    url(r'^logout/',log_out),
    url(r'^feed/', feed_view),
    url(r'^post/', post_view),
    url(r'^like/', like_view),
    url(r'^comment/', comment_view),
    url(r'^contactus/', contact_us),
    url(r'^$',sign_up)
]
