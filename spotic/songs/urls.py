from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ListSongView.as_view(), name='songs_list'),
    path('create/', views.CreateSongView.as_view(), name='song_create'),
    path('retrieve/', views.RetrieveSongView.as_view(), name='song_retrieve'),
    path('update/', views.UpdateSongView.as_view(), name='song_update'),
    path('delete/', views.DeleteSongView.as_view(), name='song_delete')
]