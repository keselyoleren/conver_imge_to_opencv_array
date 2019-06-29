from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    path('', include('opencvArryToJpg.urls'))

]
