from django.shortcuts import render,redirect
from .models import AboutUs,Project,ContactUs
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,"base.html")
def Menu(request):
    return render(request,"menu.html")
# def About(request):
#     return render(request,"about.html")
def Book(request):
    return render(request,"contact.html")


def About(request):
    obj=AboutUs.objects.all()
    context={"objs":obj}
    return render(request,'about.html',context)

def Contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('phonenumber')
        fdesc = request.POST.get('description')
        
        #print(f"Name: {fname}, Email: {femail}, Phone: {fphoneno}, Description: {fdesc}")
        
        
        query = ContactUs(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get back to you soon!")

        return redirect('/contact/')

    return render(request, 'contact.html')

def projects(request):
    obj=Project.objects.all()
    context={"objs":obj}
    return render(request,'menu.html',context)
