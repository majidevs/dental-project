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
    
        # Send email
        send_mail(
            message_name,#subject
            message,#message
            message_email,#from
            ['EMAIL_HOST_USER'],# to mail
            fail_silently=False,
        )

    else:
        # return the page
        return render(request, 'contact.html', {})