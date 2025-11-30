from django.urls import path, include


urlpatterns = [
    path('users/', include('users.urls')),
    path('songs/', include('songs.urls')),
    path('artists/', include('artists.urls'))
]