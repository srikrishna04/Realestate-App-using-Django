from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Listing
from .forms import ListingForm

# Create your views here.
# CRUD - list, retrieve, create, update, delete

def listings_list(request):
    index = Listing.objects.all()
    template = loader.get_template('listings.html')
    context = {
        "index": index
    }
    return HttpResponse(template.render(context, request))

def listings_retreive(request, id):
    listing = Listing.objects.get(id = id)
    template = loader.get_template('listing.html')
    context = {
        "listing" : listing
    }
    return HttpResponse(template.render(context, request))

def listings_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    template = loader.get_template('listing_create.html')
    context = {
    "form" : form
    }
    return HttpResponse(template.render(context, request))

def listings_update(request, id):
    listing = Listing.objects.get(id = id)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    template = loader.get_template('listing_update.html')
    context = {
    "form" : form
    }
    return HttpResponse(template.render(context, request))

def listings_delete(request, id):
    listing = Listing.objects.get(id = id)
    listing.delete()
    return HttpResponseRedirect("/")