from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactMessage
from django.contrib import messages


# Create your views here.
def notes(request):
    return render(request, "notes.html")

# all course
def bca(request):
    return render(request, "allsemBCA.html")
def bsc(request):
    return render(request, "allsemBSC.html")
def bcom(request):
    return render(request, "allsemBCOM.html")
def bba(request):
    return render(request, "allsemBBA.html")

# masters information
def master(request):
    return render(request, "masterscs.html")
def commers(request):
    return render(request, "mastersmc.html")

# all semester BBA
def semseter1(request):
    return render(request, "1semBBA.html")

def semseter2(request):
    return render(request, "2semBBA.html")

def semseter3(request):
    return render(request, "3semBBA.html")

def semseter4(request):
    return render(request, "4semBBA.html")

def semseter5(request):
    return render(request, "5semBBA.html")

def semseter6(request):
    return render(request, "6semBBA.html")

#all semester BCA
def sem1(request):
    return render(request,"1semBCA.html")

def sem2(request):
    return render(request,"2semBCA.html")

def sem3(request):
    return render(request,"3semBCA.html")

def sem4(request):
    return render(request,"4semBCA.html")

def sem5(request):
    return render(request,"5semBCA.html")

def sem6(request):
    return render(request,"6semBCA.html")

# all semester Bsc
def text1(request):
    return render(request,"1semBSC.html")

def text2(request):
    return render(request,"2semBSC.html")

def text3(request):
    return render(request,"3semBSC.html")

def text4(request):
    return render(request,"4semBSC.html")

def text5(request):
    return render(request,"5semBSC.html")

def text6(request):
    return render(request,"6semBSC.html")

# all semester Bcom
def semesters1(request):
    return render(request,"1semBCOM.html")

def semesters2(request):
    return render(request,"2semBCOM.html")

def semesters3(request):
    return render(request,"3semBCOM.html")

def semesters4(request):
    return render(request,"4semBCOM.html")

def semesters5(request):
    return render(request,"5semBCOM.html")

def semesters6(request):
    return render(request,"6semBCOM.html")






from django.shortcuts import render
from .models import ContactMessage

def contact(request):
    success_message = ''
    
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the data to the database
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)

        # Set the success message
      #  success_message = 'Your message has been sent successfully!'

    return render(request, 'contact.html', {'success_message': success_message})







