from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'rentapp/home.html')

def listing(request):
    return render(request , 'rentapp/listing.html')
