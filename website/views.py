from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name': message_name })
    
       
        send_mail(
            message_name,
            message,
            message_email,
            ['EMAIL_HOST_USER'],
            fail_silently=False,
        )

    else:
        # return the page
        return render(request, 'contact.html', {})
    
def service(request):
    return render(request, 'service.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blogdetails(request):
    return render(request, 'blogdetails.html', {})