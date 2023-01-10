from django import forms
from django.forms import widgets
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Event1,Event2,Bio, WorkshopBio,Workshop
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class BioForm(forms.ModelForm):
    TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
    )
    event1 = forms.ModelMultipleChoiceField(
            queryset=Event1.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
            label="Events You Want to Participate"
            )
    # iitg_student = forms.BooleanField(widget=forms.Select(),label="Are you IIT Guwahati Student", required=True)
    iitg_student = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Are you IIT Guwahati Student", initial='', widget=forms.Select(), required=True)
    number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))
    class Meta:
        model = Bio
        fields = ("institute","dept","iitg_student","abstract","event1","event2","number")
        labels = {
            "institute": "Please Enter your institute (Note: Please Enter Your institute name in Block Letters) *",
            "dept": "Please Select your related Department *",
            "abstract": "Please upload your Abstract file in .pdf format *",
            "event2": "Event (Poster/Oral) you want to participate  (Note: if you are not selected in Oral Presentation then you will be automatically allowed to participate in Poster Presentation)",
        }   


class AbstractForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ("abstract",)


class WorkshopForm(forms.ModelForm):
    workshop = forms.ModelMultipleChoiceField(
            queryset=Workshop.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            label="Events You Want to Participate"
            )
    number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IN'))
    class Meta:
        model = WorkshopBio
        fields = ("dept","workshop","number")


class WorkshopPaymentDetailForm(forms.ModelForm):
    class Meta:
        model = WorkshopBio
        fields = ("razorpay_payment_id",)
