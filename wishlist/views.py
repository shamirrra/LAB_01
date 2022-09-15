# Lab 1
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Lab 2
from django.http import HttpResponse
from django.core import serializers

# Lab 1
data_barang_wishlist = BarangWishlist.objects.all()

context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Shamira'}
    
def show_wishlist(request):
    return render(request, "wishlist.html", context)

# Lab 2
data = BarangWishlist.objects.all()

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
