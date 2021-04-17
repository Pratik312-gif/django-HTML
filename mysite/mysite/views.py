from django.http import HttpResponse
from django.shortcuts import render
def index(request):
             values = {'name':'Pratik shete', 'age':22, 'city':'pune','collage':'zeal collage'}
             return render(request, 'home.html', values)