from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Sponsor, OurSponsor
# Create your views here.

class SponsorListView(ListView):
    model = Sponsor
    template_name = "sponsor/list.html"

    def get_context_data(self, **kwargs):
        context = super(SponsorListView, self).get_context_data(**kwargs)
        context['oursponsor_list'] = OurSponsor.objects.all()
        return context
