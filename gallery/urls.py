from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^today/$',views.gallery_today,name = 'galleryToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})$',views.past_days_gallery,name = 'pastGallery')
    
]