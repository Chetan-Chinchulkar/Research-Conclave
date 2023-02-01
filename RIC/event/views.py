from django.shortcuts import render
from .models import Product,Speaker,InstituteSpeaker
from members.models import Workshop
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
# Create your views here.

class ProductDetail(DetailView):
    model = Product
    template_name='event/detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workshop_list"] = Workshop.objects.all()
        return context


class SpeakerDetail(DetailView):
    model = Speaker
    template_name='event/speaker.html'



class InstituteSpeakerListView(ListView):
    model = InstituteSpeaker
    template_name = "event/institutespeakerlist.html"


class InstituteSpeakerDetailView(DetailView):
    model = InstituteSpeaker
    template_name='event/institutespeakerdetail.html'
    
