from django.urls import path

from images.views import images_views, images_detail_view, save_image_view


app_name = 'images'
urlpatterns = {
    path('post/<int:img_id>/', images_detail_view, name='detail'),
    path('', images_views, name='img'),
    path('save-image/', save_image_view, name='save_image'),
}

