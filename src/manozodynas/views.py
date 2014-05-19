from django.shortcuts import render
from manozodynas.models import Age
from django.views.generic.edit import CreateView


def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def zodziai_view(request):
    zodziai = Age.objects.all()
    return render(request, 'manozodynas/zodziai.html', {'zodziai': zodziai})

class IvestiView(CreateView):
    model = Age
    fields = ['age']
    success_url = '/zodziai/'
