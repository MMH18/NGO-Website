from pickle import GET
from urllib.request import Request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import contact,contacts





from math import prod


import decimal

# Create your views here.

# def list_products(request):
#     all_products = product.objects.all()
#     return render(request,"products/list-products.html",{'products':'all_products'})






def Contact_us(request):
    # if request.method == "POST":
    #     print("request : post!")
    all_contacts = contacts.objects.all()
    if request.method == "GET":
        return render(request, "contact-us.html", {'contacts': 'all_contacts'})
    else:
        print(request.method)
        firstname= request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        desc = request.POST.get('desc')
        is_true = request.POST.get('is_true')
            


        

        message = contacts.objects.create(
            firstname=firstname, lastname=lastname,
            email=email, address1=address1,
            address2=address2, city=city,
            zip=int(zip),desc=desc,is_true=bool(is_true)
        )
        # product.save()
    
        return redirect(reverse_lazy('contact_us_response'))
    

def project(request):
    return render(request,"projects.html")
def who_we_are(request):
    return render(request,"who-we-are.html")
def our_team(request):
    return render(request,"our-team.html")
def home_page(request):
    return render(request,"index.html")
def contact_us_response(request):
    return render(request,"contact-us-response.html")
# @login_required
# def HTML_code(request):
#     if request.user.is_authenticated:
#         return render(request, "index.html", {"greeting": "Hello world"})
#     else:
#         return HttpResponse("Please Login First")