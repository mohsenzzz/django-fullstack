from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import User
# Create your views here.

def get_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request,'users/users.html',context=context)
