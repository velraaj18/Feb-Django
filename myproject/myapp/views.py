from django.shortcuts import render
from .models import Dog
# Create your views here.

def index(request):
   dogs = Dog.objects.all()
   return render(request ,'index.html', {'dogs':dogs})

def counter(request):
   text = request.POST['text']
   amount_of_words = len(text.split())
   return render(request, 'counter.html', {'amount_of_words' : amount_of_words})