from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'top.html')

@login_required
def create(request):
    return render(request, 'create.html')