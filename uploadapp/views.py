from django.http import HttpResponse
from django.shortcuts import render
from uploadapp.forms import UploadFileForm, UploadForm

from uploadapp.models import Upload

# Create your views here.


def uploadStart(request):
    return HttpResponse("<h1>started new upload app</h1>")


def upload_form(request):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_image.html', {'form': form, "saved_object": saved_object})
    else:
        form = UploadForm()
    context = {"form": form}
    return render(request, 'uploadapp/add_image.html', context)


def upload_files(request):
    form = UploadFileForm()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_files.html', {'form': form, "saved_object": saved_object})
    else:
        form = UploadFileForm()
    context = {"form": form}
    return render(request, 'uploadapp/add_files.html', context)
