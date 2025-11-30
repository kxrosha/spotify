from django.urls import path
from . import views


urlpatterns = [
    path('create', views.CreateArtistsView.as_view(), name='create_artist'),
    path('list', views.ListArtistsView.as_view(), name='list_artists'),
    path('<int:pk>', views.RetrieveUpdateDeleteArtistsView.as_view(), name='update_delete_retrieve_artists')
]