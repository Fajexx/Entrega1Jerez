from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(
        request=request,
        context={},
        template_name='home/index.html'
    )

