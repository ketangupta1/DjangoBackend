from django.urls import path
from . import views

urlpatterns = [
    path('', views.dummy_view),
    path('view_<int:view_num>', views.dummy_view_num),
    path('view_kwargs_<int:num>', views.dummy_view_kwargs, {"Key":"Ketan"})
]
