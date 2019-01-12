from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views import View

# Create your views here.

USER_DICT = {
    '1':{'user':'root1','email':'root@live.com'},
    '2':{'user':'root2','email':'root@live.com'},
    '3':{'user':'root3','email':'root@live.com'},
    '4':{'user':'root4','email':'root@live.com'},
}

# def detial(request):
#
#     nid = request.GET.get('nid')
#     detial_info = USER_DICT[nid]
#     return render(request,'detial.html',{'detial_info':detial_info})
def detial(request,nid):
    detial_info = USER_DICT[nid]
    return render(request,'detial.html',{'detial_info':detial_info})

def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})

# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         u = request.POST.get('user')
#         p = request.POST.get('pwd')
#         if u == 'alex' and p == '123':
#             return redirect('/index/')
#         else:
#             return render(request,'login.html')
#     else:
#         return redirect('/index/')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # v = request.POST.get('gender')
        # print(v)
        # v = request.POST.getlist('favor')
        # print(v)
        # v2 = request.POST.getlist('city')
        # print(v2)
        # v = request.POST.get('fawenjian')
        # print(v)
        v2 = request.FILES.get('fawenjian')
        print(v2,type(v2),v2.name)
        import os
        file_path=os.path.join('upload',v2.name)
        f = open(file_path,mode='wb')
        for i in v2.chunks():
            f.write(i)
        f.close()
        return render(request,'login.html')
    else:
        return redirect('/index/')


class Home(View):

    def dispatch(self, request, *args, **kwargs):
        #调用父类中的dispatch
        print('before')
        result = super(Home,self).dispatch(request,*args,**kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method,'POST')
        return render(request,'home.html')



