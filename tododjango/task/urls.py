from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('task/', views.index),
    path('task/delete/<slug:id>', views.delete_task),
    path('',RedirectView.as_view(url='task/'))
]