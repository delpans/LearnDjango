from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from django.views import View


def index(request):
    """

    index视图函数
    :param request:request是HttpRequest对象，包含前端用户的所有请求信息
    :return:必须返回一个HttpResponse对象或者子对象
    """
    if request.method == "GET":
        #此处好几百行代码
        return HttpResponse("<h1>GET请求：hello，python测开大佬们</h1>")
    elif request.method == "POST":
        #此处好几千行代码
        return HttpResponse("<h1>POST请求：hello，python测开大佬们</h1>")
    else:
        #此处有好几万行代码
        return HttpResponse("<h1>其他请求：hello，python测开大佬们</h1>")



#类视图
class IndexView(View):
    """
    index主页类视图

    """
    def get(self,request):
        #get请求
        # return HttpResponse("<h1>GET请求：hello，python测开大佬们</h1>")
        return render(request, 'demo.html')

    def post(self,request):
        return HttpResponse("<h1>POST请求：hello，python测开大佬们</h1>")

    def delete(self,request):
        return HttpResponse("<h1>DELETE请求：hello，python测开大佬们</h1>")

    def put(self,request):
        return HttpResponse("<h1>PUT请求：hello，python测开大佬们</h1>")