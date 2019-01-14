from django.urls import path
# from . import views
from project import views
app_name = 'project'
urlpatterns = [
    path('', views.form_index, name='index'),
    path('similarity/', views.form_index),
]