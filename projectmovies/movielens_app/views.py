from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def my_view(request):
    # Your view logic here
    return render(request, 'my_template.html')
