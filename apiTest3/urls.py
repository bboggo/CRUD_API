"""apiTest2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include, re_path
from equipApi import views
#from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

app_name = 'equipApi'

#router = routers.DefaultRouter() 
#router.register('equipment', equipViewSet)
#router.register('equipment-detail', detailViewSet)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path(r'^$', views.equipView.as_view(), name='equip'),
    re_path(r'^equipment/$', views.equipView.as_view(), name='equipment'),
    re_path(r'^equipment/create/$', views.createView.as_view(), name='equipment-create'),
    re_path(r'^equipment/(?P<no>\d+)/$', views.detailView.as_view(), name='equipment-detail'),
    re_path(r'^equipment/(?P<no>\d+)/update$', views.updateView.as_view(), name='equipment-update'),    
    re_path(r'^equipment/(?P<no>\d+)/delete$', views.deleteView.as_view(), name='equipment-delete'),

    re_path(r'^information/$', views.inforView.as_view(), name='information'),
    re_path(r'^information/create/$', views.inforcreateView.as_view(), name='information-create'),
    re_path(r'^information/(?P<no>\d+)/$', views.infordetailView.as_view(), name='information-detail'),
    re_path(r'^information/(?P<no>\d+)/update$', views.inforupdateView.as_view(), name='information-update'),    
    re_path(r'^information/(?P<no>\d+)/delete$', views.infordeleteView.as_view(), name='information-delete'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)