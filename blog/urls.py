from django.urls import path
from . import views

#adesso aggiungiamo una view chiamata post_list, quindi se una persona accede al link, verrà reindirizzato a views.post_list
urlpatterns = [
    path('', views.post_list, name = 'post_list'), #post_list è il nome della url che verrà usata per identificare la views
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]