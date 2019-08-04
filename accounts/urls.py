from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    # You can only see your profile
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/delete', views.ProfileDeleteView.as_view(), name='delete'),
]
