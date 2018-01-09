#django imports
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

# project imports
from .models import Url

class UrlCreateView(CreateView):
    model=Url
    template_name='main.html'
    fields=['user_input']

class UrlDetailView(DetailView):
    model=Url
    slug_url_kwarg='shortened_url_ending'
    slug_field='shortened_url_ending'

def redirect_view(request, shortened_url_ending):
    url_redirect_to = "https://" + Url.objects.get(shortened_url_ending=shortened_url_ending).url_redirect_to
    return redirect(url_redirect_to)
