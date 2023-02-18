from django.urls import path

from images.views import images_views, images_detail_view


app_name = 'images'
urlpatterns = [
    path('post/<int:img_id/', images_detail_view, name='detail'),
    path('', images_views, name='img')
]

