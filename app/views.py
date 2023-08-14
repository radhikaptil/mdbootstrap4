from django.shortcuts import render

# Create your views here.
def mdb4(request):
    return render(request,'mdb4.html')

def button(request):
    return render(request,'button.html')

def carousel(request):
    return render(request,'carousel.html')

def card(request):
    return render(request,'card.html')
