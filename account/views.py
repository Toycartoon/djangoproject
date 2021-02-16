from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from account.models import Data_Model, Photo


def index(request):
    if request.method == "POST":
        form = Data_Model()
        form.uid = request.POST["uid"]
        form.passwd = request.POST["passwd"]
        form.pub_date = timezone.datetime.now()
        form.save()
        for img in request.FILES.getlist('image'):
            photo = Photo()
            photo.data = form
            photo.image = img
            photo.save()

        return redirect('show/' + str(form.uid), form.uid)
    else:
        return render(request, 'index.html')


def show(request, form_id):
    lst = get_object_or_404(Data_Model, pk=form_id)
    return render(request, 'show.html', {'lst':lst})
