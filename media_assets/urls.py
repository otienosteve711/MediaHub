from django.urls import path
from . import views
# create the namespace for our urls
app_name = 'media_assets'

urlpatterns = [
    # '' : root path : 8000/ 
    path('', views.dashboard_view, name='dashboard'),
    path('my_media/', views.my_media_view, name='my_media'),# users uploaded media files view
    path('upload/', views.upload_media_view, name='upload_media'),# users upload media files view
    path('media/<int:pk>/', views.media_detail_view, name='media_detail'),# media full detail view
    path('media/<int:pk>/edit/', views.edit_media_view, name='edit_media'),# media edit view
    path('media/<int:pk>/delete/', views.delete_media_view, name='delete_media'),# media delete view

]