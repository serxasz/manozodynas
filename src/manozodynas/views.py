from django.shortcuts import render
from manozodynas.models import Age
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import login

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def zodziai_view(request):
    zodziai = Age.objects.all()
    return render(request, 'manozodynas/zodziai.html', {'zodziai': zodziai})

class IvestiView(CreateView):
    model = Age
    fields = ['age']
    success_url = '/zodziai/'

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    #import ipdb; ipdb.set_trace()
    return render(request, 'manozodynas/login.html', {'form':form})
