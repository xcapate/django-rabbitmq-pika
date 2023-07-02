from django.urls import path

from .views import DefaultView

urlpatterns = [
    path('', DefaultView.as_view(), name='default'),
]
