from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})
    # return HttpResponse("<h1>안녕하세요. 나는 송하선입니다. 당신을 만나 반갑습니다.!</h1>")