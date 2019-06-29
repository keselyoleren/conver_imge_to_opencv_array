from django.conf.urls import include, url 
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    path('', views.index, name='index'),
    path('img-to-opencv', views.img_to_opencv, name='image-to-opencv'),
    path('opencv-to-image', views.opencv_to_img, name='opencv-to-image')
]
