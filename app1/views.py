from django.shortcuts import render

# Create your views here.
def components(request):
    return render(request,'components.html')

def carousel(request):
    return render(request,'carousel.html')