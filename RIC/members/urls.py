from django.urls import path, reverse_lazy
from . import views


app_name='members'
urlpatterns = [
    path('', views.ProfileListView.as_view(),name='all'),
    path('create/', views.ProfileCreateView.as_view(),name='create'),
    path('workshop_create/', views.WorkshopCreateView.as_view(),name='workshop_create'),
    path('detail/<int:pk>/', views.ProfileDetailView.as_view(),name='detail'),
    path('workshop_detail/<int:pk>/', views.WorkshopDetailView.as_view(),name='workshop_detail'),
    path('abstract/<int:pk>', views.AbstractUpdateView.as_view(),name='abstract'),

]