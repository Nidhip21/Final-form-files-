from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.

def index(request):
    return HttpResponse("Welcome :) This is my first Django project")


def nidhi(resquest):
    return HttpResponse("Wow! Its working!")

def template(request):
    dict_var = {'random_var':'I am from views.py'}
    return render(request,'firstapp/index.html',context=dict_var)

def form_view(request):
    form = forms.FormName()
    if reques.method=="POST":
       form = forms.FormName(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponse("done")
       else:
           print(form.erroes)
           return render(request, 'firstweb/basic_form.html', {'formal:form'})
    return render(request, 'firstweb/basic_form.html',{'formal:form'})





