import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html')

def about(request):
    return render_to_response('home/about.html')

def user(request):
    from openshift.shims.user import files
    return render_to_response('home/user.html', {
        'files': files
    })

def marketplace(request):
    return render_to_response('marketplace.html')

