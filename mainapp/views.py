from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
import requests

api_url = "http://127.0.0.1:8000/api/"


class BaseView(View):
    def get(self, request):
        coffins = requests.get(api_url + "coffin").json()
        return render(request, 'base.html', context={'coffins': coffins})


class RequestView(View):
    def get(self, request):
        request_request = requests.get(api_url + "requests").json()
        return render(request, 'request.html', context={'request_request': request_request})

    def post(self, request):
        if request.method == "POST":
            payload = {
                "full_name": request.POST['full_name'],
                "phone": request.POST['phone'],
                "email": request.POST['email'],
                "service": request.POST['service'],
                "date_of_funeral": request.POST['date_of_funeral'],
                "price_of_funeral": request.POST['price_of_funeral'],
                "about": request.POST['about'],
            }
            status_code = requests.post(api_url + "requests", json=payload)
            if status_code.status_code != 200:
                return redirect('home')
            else:
                return HttpResponseRedirect('/')
        return render(request, 'request.html', {'request': list})


class CoffinListView(View):
    def get(self, request):
        coffins = requests.get(api_url + "coffin").json()
        return render(request, 'breed_list.html', context={'coffins': coffins})


class AboutView(View):
    def get(self, request):
        coffins = requests.get(api_url + "coffin").json()
        return render(request, 'about.html', context={'coffins': coffins})


def index(request):
    return render(request, 'index.html', {})


# def breed_detail(request, id):
#     return render(request, 'index.html', {})
#
#
# def form_detail(request, id):
#     return render(request, 'index.html', {})
