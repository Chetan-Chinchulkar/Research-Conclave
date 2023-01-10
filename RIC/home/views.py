from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from event.models import Product
from team.models import Team
from sponsor.models import OurSponsor
from .models import About
# Create your views here.


class LoginView(TemplateView):
    template_name = "home/test.html"

class AboutList(ListView):
    model = About
    template_name='home/about.html'


class ProductListView(ListView):
    model = Product
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['team_list'] = Team.objects.all()
        context['about_list'] = About.objects.all()
        context['sponsor_list'] = OurSponsor.objects.all()
        return context