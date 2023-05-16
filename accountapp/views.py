from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        if request.POST.get('hello_world_input') == '':
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            temp = request.POST.get('hello_world_input')
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
            # hello_world_list = HelloWorld.objects.all()
            # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    # return HttpResponse("<h1>안녕하세요. 나는 송하선입니다. 당신을 만나 반갑습니다.!</h1>")