"""wgt_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from golf_course import urls as golf_course_urls
from golfer import urls as golfer_urls
from tournament import urls as tournament_urls
from golfer_polls import urls as golfer_polls_urls
from .views import homepage


urlpatterns = [
    url(r'^$', homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^golf_course/', include(golf_course_urls)),
    url(r'^golfer/', include(golfer_urls)),
    url(r'^tournament/', include(tournament_urls)),
    url(r'^golfer_polls/', include(golfer_polls_urls)),
    url(r'^', include(golf_course_urls)),

]

admin.site.site_header = "Wake Golf Tour"
admin.site.index_title = "WGT Site Administration"