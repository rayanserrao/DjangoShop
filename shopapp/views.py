from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'test.html')



@csrf_exempt
def postdata(request):
    a=request.POST.get('uname')
    b=request.POST.get('address')
    c=request.POST.get('choose')
    d=request.POST.get('qty')
    d=int(d)
    e=d*200
    f=e*0.8

    return render(request,"success.html",{'a':a,'b':b,'c':c,'e':e,'f':f})
    # msg="Hi "+a+" you adress is "+b+ "you have chosesn"+c+ " and the total cost is "+str(e*200)
    # return HttpResponse(msg)


