from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_record, name='add'),
    path('show', views.show_records, name='show'),
]