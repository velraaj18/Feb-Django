from django.shortcuts import render

# Create your views here.

def index(request):
   context ={
      'name': 'vel',
      'age' : 21,
      'Degree': 'B.E'
   } 
   return render(request ,'index.html', context)