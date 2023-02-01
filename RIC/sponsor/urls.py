from django.urls import path, reverse_lazy
from . import views


app_name='sponsor'
urlpatterns = [
    path('', views.SponsorListView.as_view(),name='all'),

]