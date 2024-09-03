from django.shortcuts import render
from .forms import InfoItem
from .models import *

# Create your views here.
def home(request):
    form1= InfoItem()
    if request.method=='POST':
        form=InfoItem(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    data1= resume.objects.all()
    return render(request,'home.html',{'form1':form1,'data1':data1})
