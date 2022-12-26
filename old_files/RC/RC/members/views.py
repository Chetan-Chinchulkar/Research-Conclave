import json
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Event1,Event2,Bio,WorkshopBio
from .forms import BioForm,AbstractForm,WorkshopForm
import razorpay
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProfileListView(LoginRequiredMixin, ListView):
    model = Bio
    template_name = "members/profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workshop_bio"] = WorkshopBio.objects.all()
        return context
    


class ProfileCreateView(LoginRequiredMixin,CreateView):
    form_class = BioForm
    template_name = 'members/profile_create.html'
    def get_success_url(self):
        return reverse('members:all')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        pic = form.save(commit=False)
        pic.save()
        form.save_m2m()
        temp=0
        for i in form.instance.event1.all():
            temp=temp+i.fee
        print(temp)  
        temp=temp+form.instance.event2.fee
        print(temp)  
        form.instance.total = temp
        return super().form_valid(form)

@method_decorator(csrf_exempt,name='dispatch')
class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = Bio
    template_name = "members/profile_detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        client = razorpay.Client(auth=("rzp_test_5yvtSG4kkzANL2", "DmdWo45YVkEIfxTObkiw28hx"))
        DATA = {    
            "amount": self.object.total,    
            "currency": "INR",    
            "receipt": "receipt#1",    
            "notes": {        
                "key1": "value3",        
                "key2": "value2"    
                }
            }
        x = client.order.create(data=DATA)
        self.object.razorpay_order_id=x
        context['order'] = x['id']
        context['rupee'] = self.object.total/100
        return context

    def post(self,request,*args,**kwargs):
        a = json.loads(request.body.decode('utf-8'))
        print(a['payment_id'])
        print(type(self.get_object()))
        self.get_object().setpaymentid(a['payment_id'])  
        # self.get_object().save()
        print(self.get_object().razorpay_payment_id)
        return JsonResponse({
              "message":"Worked fine"
            })


# class AbstractUpdateView(LoginRequiredMixin,UpdateView):
#     model = Bio
#     template_name = "members/update.html"
#     success_url = reverse_lazy('members:all')
#     fields = ['abstract']

#     def post(self, request, pk=None):
#         pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
#         request.POST = request.POST.copy()
#         request.POST['abstractFormat'] = 'Yes'
#         return super(AbstractUpdateView, self).post(request, **kwargs)
class AbstractUpdateView(LoginRequiredMixin, View):
    template_name = 'members/update.html'
    success_url = reverse_lazy('members:all')
    def get(self, request, pk) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = AbstractForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        pic = get_object_or_404(Bio, id=pk, owner=self.request.user)
        form = AbstractForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.abstractFormat =True
        pic.save()
        form.save_m2m()

        return redirect(self.success_url)


class WorkshopCreateView(LoginRequiredMixin,CreateView):
    form_class = WorkshopForm
    template_name = 'members/workshop_create.html'
    def get_success_url(self):
        return reverse('members:all')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        pic = form.save(commit=False)
        pic.save()
        form.save_m2m()
        temp=0
        for i in form.instance.workshop.all():
            temp=temp+i.fee
        form.instance.total = temp
        return super().form_valid(form)

@method_decorator(csrf_exempt,name='dispatch')
class WorkshopDetailView(LoginRequiredMixin,DetailView):
    model = WorkshopBio
    template_name = "members/workshop_detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        client = razorpay.Client(auth=("rzp_test_5yvtSG4kkzANL2", "DmdWo45YVkEIfxTObkiw28hx"))
        DATA = {    
            "amount": self.object.total,    
            "currency": "INR",    
            "receipt": "receipt#1",    
            "notes": {        
                "key1": "value3",        
                "key2": "value2"    
                }
            }
        x = client.order.create(data=DATA)
        context['order'] = x['id']
        context['rupee'] = self.object.total/100
        return context

    def post(self,request,*args,**kwargs):
        a = json.loads(request.body.decode('utf-8'))
        print(a['payment_id'])
        print(type(self.get_object()))
        self.get_object().setpaymentid(a['payment_id'])  
        # self.get_object().save()
        print(self.get_object().razorpay_payment_id)
        return JsonResponse({
              "message":"Worked fine"
            })