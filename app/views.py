from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

# FBV for returning string
def fbv_string(request):
    return HttpResponse(' This is function view')
# CBV for returning string
class CBV_STRING(View):
    def get(self,request):
        return HttpResponse('This is class view')
    
# FBV for returning HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')
# CBV for returning HTML page
class CBV_HTML(View):
    def get(self,request):
        return render(request,'CBV_HTML.html')
# Handling forms by using FBV
def fbv_form(request):
    TO=Topicform()
    d={'TO':TO}
    if request.method=='POST':
        TFD=Topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')
    return render(request,'fbv_form.html',d)

# Handling forms by using CBV
class CBV_FORM(View):
    def get(self,request):
        TO=Topicform()
        d={'TO':TO}
        return render(request,'CBV_FORM.html',d)
    def post(self,request):
        TFD=Topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')