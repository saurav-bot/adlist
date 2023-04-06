from django.shortcuts import render
from ads.owner import OwnerCreateView, OwnerListView, OwnerDeleteView, OwnerDetailView, OwnerUpdateView
from ads.models import Ad
from django.urls import reverse_lazy

# Create your views here.

class AdListView(OwnerListView):
    model = Ad 

class AdDetailView(OwnerDetailView):
    model = Ad 
    
class AdCreateView(OwnerCreateView):
    model = Ad 
    fields = ['title', 'text', 'price']
    success_url = reverse_lazy('ads:all')

class AdUpdateView(OwnerUpdateView):
    model = Ad 
    fields = ['title', 'text', 'price']
    success_url = reverse_lazy('ads:all')

class AdDeleteView(OwnerDeleteView):
    model = Ad 
    success_url = reverse_lazy('ads:all')
