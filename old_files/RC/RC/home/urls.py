from django.urls import path, reverse_lazy
from . import views


app_name='home'
urlpatterns = [
   path('', views.ProductListView.as_view(),name='home'),
   path('about', views.AboutList.as_view(),name='about'),
   path('register', views.LoginView.as_view(),name='redirection'),
]