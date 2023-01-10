from django.urls import path, reverse_lazy
from . import views


app_name='event'
urlpatterns = [
    path('<int:pk>', views.ProductDetail.as_view(),name='detail'),
    path('workshopspeaker/<int:pk>', views.SpeakerDetail.as_view(),name='workshopspeakerspeaker'),
    path('speaker/', views.InstituteSpeakerListView.as_view(),name='speakerlist'),
    path('speaker/<int:pk>', views.InstituteSpeakerDetailView.as_view(),name='speakerdetail'),
    
]