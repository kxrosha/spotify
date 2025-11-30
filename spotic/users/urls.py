from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from . import views


urlpatterns = [
    path('', views.ListUserView.as_view(), name='users_list'),
    path('register/', views.CreateUserView.as_view(), name='user_register'),
    path('retrieve/<int:pk>/', views.RetrieveUserView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', views.UpdateUserView.as_view(), name='user_update'),
    path('delete/<int:pk>/', views.DeleteUserView.as_view(), name='user_delete'),


    
    path('token/login/', TokenObtainPairView.as_view(), name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='user_refresh_token'),
    path('token/verify/', TokenVerifyView.as_view(), name='user_verify_token'),
    path('token/logout/', TokenBlacklistView.as_view(), name='user_logout')
]