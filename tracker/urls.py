from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.log_view, name='log_view'),
]