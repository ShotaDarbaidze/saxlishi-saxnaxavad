from django.shortcuts import render

def ip_address_processor(request):
    return{"ip_address": request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_address_processor(request))

def user(request):
    username = 'x'
    password = '1234'
    email = 'abc@gmail.com'
    age = "15"
    height = "165"
    context = {
        'username':username,
        'password':password,
        'email': email,
        'age': age,
        'height': height
    }
    return render (request,'user.html',context = context)
    
