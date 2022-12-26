from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from home.models import About


class ScheduleView(ListView):
    model = About
    template_name = "schedule/list.html"
