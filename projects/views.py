from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.db.models import Q

from projects.models import Projects


def index(request):
    """

    index视图函数
    :param request:request是HttpRequest对象，包含前端用户的所有请求信息
    :return:必须返回一个HttpResponse对象或者子对象
    """
    if request.method == "GET":
        # 此处好几百行代码
        return HttpResponse("<h1>GET请求：hello，python测开大佬们</h1>")
    elif request.method == "POST":
        # 此处好几千行代码
        return HttpResponse("<h1>POST请求：hello，python测开大佬们</h1>")
    else:
        # 此处有好几万行代码
        return HttpResponse("<h1>其他请求：hello，python测开大佬们</h1>")


# 类视图
class IndexView(View):
    """
    index主页类视图

    """

    # def get(self,request):
    #     #get请求
    #     # return HttpResponse("<h1>GET请求：hello，python测开大佬们</h1>")
    #     return render(request, 'demo.html')

    # def get(self,request):
    #     #1、可以使用request.GET
    #     #2、request.GET返回的是一个类字典对象，支持字典中的所有操作
    #     #3、查询字符串参数中。如果有多个相同的key，使用request.GET获取的是最后一个值
    #     #4、使用request.GET.geilist('name')可以获取多个相同key值的参数
    #     return HttpResponse("<h1>GET请求：hello，python测开大佬们</h1>")

    def get(self, request):
        # 创建数据
        # 方法一：
        # 创建模型类对象,还未执行sql语句
        # one_obj = Projects(name='这是一个牛逼的项目522', leader='icon', programer='弱音', publish_app='这是一个厉害的应用', desc='无描述')
        # 调用save方法保存，才去数据库中执行sql
        # one_obj.save()

        # 方法二：
        # Projects.objects.create(name='这是一个牛逼的项目525', leader='icon111', programer='弱音520', publish_app='这是一个厉害的应用', desc='无描述')

        # 1、获取一个数据的所有记录
        # QuerySet查询集，就相当于一个列表（存放所有项目对象的列表）
        # qs=Projects.objects.all()
        # for i in qs:
        #     print(f"{type(i)}")
        #     print(f"{i.name}")

        # 2、获取某一个指定的记录，get()
        # get方法只能返回一条记录
        # 如果返回多条记录或者查询的记录不存在那么会抛出异常
        # get方法的参数往往为主键或者唯一键
        # one_project=Projects.objects.get(id=1)

        # 3、获取某一些记录，filter（）或者exclude（）
        # 使用filter获取的是满足条件之后的queryset查询集，exclude是不满足条件的queryset查询集
        # qs=Projects.objects.filter(leader__contains='icon')

        # 使用特定的过滤方法
        # 模型类属性（字段名）__contains包含指定字符串的所有记录返回
        # leader__icontains忽略大小写
        # 将startswith以给定字符串开头的所有记录返回
        # 将endswith以给定字符串结尾的所有记录返回
        # 将in以给定范围的字符串的所有记录返回
        # qs = Projects.objects.filter(leader__contains='icon')
        # qs = Projects.objects.filter(leader__icontains='icon')
        # qs = Projects.objects.filter(leader__startswith='i')
        # qs = Projects.objects.filter(leader__in=['icon','icon111'])

        # 4、关联查询
        # 外键字段__从表的字段名__contains
        # qs=Projects.objects.filter(interfaces__name='登录接口')

        # 5、比较查询
        # __gt   >
        # __gte  >=
        # __lt   <
        # __lte  <=
        # qs=Projects.objects.filter(id_gt=2)

        # 6、逻辑关系，多个条件查询
        # 如果给filter指定多个条件，那么条件之间是与的关系
        # qs=Projects.objects.filter(leader='icon', name__contains='牛逼')

        # 可以使用Q变量指定多个条件，那么条件之间是或的关系
        # qs = Projects.objects.filter(Q(leader='icon') | Q(name__contains='牛逼'))

        # 7、查询集操作
        # 查询集相当于一个列表，支持列表中的大多数操作（通过数字索引获取值，正向切片，for循环）
        # 查询集是对数据库操作的一种优化
        # 查询集会缓存结果
        # 惰性查询
        # 查询集还支持链式操作
        # qs=Projects.objects.filter(leader__contains='icon').first()
        # qs.filter(prgramer='孤影')

        # 8、更新操作
        # a,先获取到要修改的模型对象
        # b.然后修改
        # c.保存
        # one_project = Projects.objects.get(id=1)
        # one_project.leader = '逆旅'
        # one_project.save()

        # 9.删除操作
        # a.先获取到要删除的模型对象
        # b.删除
        # c.保存
        # qs = Projects.objects.filter(name__contains='521')
        # one_project = qs.first()
        # one_project.delete()

        #10.排序操作
        #在字段名前面加-号，代表从大到小排序
        #默认是从小到大排序
        #Projects.objects.filter(id__gte=3).order_by('name')

        pass

        return JsonResponse("<h1>POST请求：hello，python测开大佬们</h1>")

    def post(self, request):
        # 1、使用request.POST['age']获取www-form表单参数
        # json格式的数据存放在body中，可以使用request.body来获取

        import json
        # 2、将bytes类型转化为字符串
        one_str = request.body.decode('utf-8')
        # 3、json格式的字符串转化为字典
        one_dict = json.loads(one_str)
        print(type(one_str))
        print(one_str)
        print(type(one_dict))
        print(one_dict)
        return HttpResponse("<h1>POST请求：hello，python测开大佬们</h1>")

    def delete(self, request):
        return HttpResponse("<h1>DELETE请求：hello，python测开大佬们</h1>")

    def put(self, request):
        return HttpResponse("<h1>PUT请求：hello，python测开大佬们</h1>")
