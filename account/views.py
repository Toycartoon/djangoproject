from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from account.models import Data_Model


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        form = Data_Model()
        form.name = name
        form.text = text
        form.save()
        lst = Data_Model.objects.all()
        return HttpResponseRedirect(reverse('index'))
    else:
        lst = Data_Model.objects.all()
        return render(request, 'index.html')


def show(request):
    lst = Data_Model.objects.all()
    return render(request, 'show.html', {'lst':lst})