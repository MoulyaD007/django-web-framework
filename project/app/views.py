from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        desc=request.POST.get('desc')
        myusercontact=Contact(name=name,email=email,phone=phone,desc=desc)
        myusercontact.save()
        return HttpResponse("response has been recorded")
    return render(request,'contact.html')