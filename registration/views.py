from django.shortcuts import render
from django import forms

# Create your views here.


class RegForm(forms.Form):
    company_name = forms.CharField(label="Company_Name")
    number_attending = forms.IntegerField(label="N.O Attending")
    date = forms.DateField(label="Date")


def index(request):
    return render(request, 'registration/index.html')


def add(request):
    return render(request, "registration/add.html", {
        "form": RegForm
    })
