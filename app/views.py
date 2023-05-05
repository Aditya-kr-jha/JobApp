from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from app.models import jobPost

# Create your views here.


job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]


class TempClass:
    x = 5


def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name": "Django", "age": 30, "first_list": list, "temp_object": temp,
               "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)


def job_list(request):
    jobs = jobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    print(type(id))

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job = jobPost.objects.get(id=id)

        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
