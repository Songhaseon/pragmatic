from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': request.POST.get('input_text')})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})
    # return HttpResponse("<h1>안녕하세요. 나는 송하선입니다. 당신을 만나 반갑습니다.!</h1>")