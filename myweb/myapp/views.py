from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from myapp import models

# Create your views here.
user_list = []


def index(request):
    #c = {}
    #c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        #tmp = {'user':username,'pwd':password}
        #user_list.append(tmp)
        #把数据保存在数据库 heyi 20190713
        models.UserInfo.objects.create(user=username,pwd=password)
        
    user_list = models.UserInfo.objects.all()
    return render(request,'index.html', {'data':user_list})
    #return render_to_response('index.html', c)
