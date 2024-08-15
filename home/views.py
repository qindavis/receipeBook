from django.shortcuts import render

from django.http import HttpResponse



def home(request):
    
    return render(request, "home/index.html")

def about(request):
    context = {'page' : 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    print("*" * 10)
    context = {'page' : 'Success'}
    return HttpResponse("Success Page!")