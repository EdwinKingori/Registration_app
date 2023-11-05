from django.views.generic.edit import FormView
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
    context = {}
    context['form'] = RegForm()
    return render(request, "registration/add.html", {
        "form": context['form']
    })


# Creating a class_based registration view


class RegFormView(FormView):
    template_name = "add.html"
    form_class = RegForm
    success_url = 'reg_complete'

    def form_valid(self, form):
        print(form.data)
        return super().form_valid(form)


def reg_complete(request):
    return render(request, 'registration/complete.html')
