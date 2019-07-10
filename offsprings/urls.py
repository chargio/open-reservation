from django.urls import path
from .views import OffspringListView


app_name = 'offsprings'
urlpatterns = [
    path('', OffspringListView.as_view(), name='index'),
]
