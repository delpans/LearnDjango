# import json
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views import View
#
# from projects.serializer import ProjectSerializer, ProjectModelSerializer
#
# from projects.models import Projects
#
#
# class ProjectsList(View):
#     def get(self, request):
#         # 1、从数据库中获取所有的项目信息
#         project_qs = Projects.objects.all()
#
#         # 2、将数据库模型实例转化为字典类型（嵌套字典的列表）
#         # 序列化
#         # project_list = []
#         # for project in project_qs:
#         #     project_list.append(
#         #         {
#         #             'name': project.name,
#         #             'leader': project.leader,
#         #             'tester': project.tester,
#         #             'programer': project.programer,
#         #             'publish_app': project.publish_app,
#         #             'desc': project.desc
#         #         }
#         #     )
#
#         # 如果返回的是列表数据（多条数据）时，那么需要添加many=True这个参数
#         serializer = ProjectModelSerializer(instance=project_qs, many=True)
#
#         #  JsonResponse第一个参数默认只能为dict字典,如果设为其他类型，需要将safe=False
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request):
#         '''新增项目'''
#         # 1、从前端获取json格式数据，转化为python中的类型
#         # 为了严谨性，这里需要做各种复杂的校验
#         # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
#         # 反序列化过程
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data, encoding='utf-8')
#
#         serializer = ProjectModelSerializer(data=python_data)
#         # 校验前端输入的数据
#         # 调用序列化器对象is_valid方法，开始校验前端参数
#         # 如果校验成功返回True，检验失败返回False
#         # 如果raise_exception=True，那么校验失败之后，会抛出异常
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return JsonResponse(serializer.errors)
#             # 当调用is_valid方法之后，才可以调用error属性，获取娇艳的错误提示
#         # 检验成功之后的数据，可以使用validated_data属性来获得
#
#         # 2、向数据库中新增项目
#         #project = Projects.objects.create(**serializer.validated_data)
#         #1、如果创建序列化器对象的时候，只给data传参，那么调用save（）方法，
#         # 实际调用的就是序列化器对象的create()方法
#         serializer.save()
#
#
#         # 3、将模型类对象转化为字典然后返回
#         # 序列化过程
#
#         return JsonResponse(serializer.data, status=201)
#
#
# class ProjectDetail(View):
#
#     def get_object(self, pk):
#         try:
#             return Projects.objects.get(id=pk)
#         except Projects.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
#         # 省略
#         # 2、获取指定pk值的项目
#         project = self.get_object(pk)
#
#         # 3、将模型类对象转化为字典
#         # 序列化过程
#         # one_dict = {
#         #     'name': project.name,
#         #     'leader': project.leader,
#         #     'tester': project.tester,
#         #     'programer': project.programer,
#         #     'publish_app': project.publish_app,
#         #     'desc': project.desc
#         # }
#         # 1、通过模型类对象（或者查询集），传给instance可进行序列化操作
#         # 2、通过序列化器ProjectSerializer对象data属性就可以获取转化之后的字典
#         serializer = ProjectModelSerializer(project)
#         return JsonResponse(serializer.data)
#
#     def put(self, request, pk):
#         # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
#         # 2、获取ID为pk值的项目
#         project = self.get_object(pk)
#
#         # 3、从前端获取json格式数据
#         # 反序列化
#         # 为了严谨性，这里需要做各种复杂的校验
#         # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data, encoding='utf-8')
#         serializer = ProjectModelSerializer(instance=project,data=python_data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return JsonResponse(serializer.errors)
#         # 4、更新项目
#
#         #在创建序列化器对象时，如果同时给instance和data传参
#         #那么调用save（）方法，会自动化调用序列化器对象的updata方法
#         serializer.save()
#         # project.name = serializer.validated_data['name']
#         # project.leader = serializer.validated_data['leader']
#         # project.tester = serializer.validated_data['tester']
#         # project.programer = serializer.validated_data['programer']
#         # project.publish_app = serializer.validated_data['publish_app']
#         # project.desc = serializer.validated_data['desc']
#         # project.save()
#
#         # 5、将模型类对象转化为字典
#         # 序列化
#         #serializer = ProjectSerializer(project)
#         return JsonResponse(serializer.data, status=201)
#
#     def delete(self, request, pk):
#         # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
#         # 2、获取ID为pk值的项目
#         project = self.get_object(pk)
#         project.delete()
#         return JsonResponse(None, safe=False, status=204)


# 注释版
# import json
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views import View
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status, filters
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from projects.serializer import ProjectSerializer, ProjectModelSerializer
#
# from projects.models import Projects
# from utils.pagination import PageNumberPaginationManual
#
#
# class ProjectsList(GenericAPIView):
#     # 1、必须指定queryset和serializer_class
#     # queryset用于指定需要使用的查询集
#     queryset = Projects.objects.all()
#     # 2、serializer_class指定需要使用到的序列化器类
#     serializer_class = ProjectModelSerializer
#
#     # 3、、在视图类中指定过滤引擎
#     #filter_backends = [filters.OrderingFilter]
#     # 4、、指定需要排序的字段
#     ordering_fields = ['name', 'leader']
#
#     #5、在类视图中指定过滤引擎
#     #filter_backends = [DjangoFilterBackend]
#
#     #6、指定需要过滤的字段
#     filterset_fields=['name','leader','tester']
#
#     #7、在某个视图中指定分页类
#     #pagination_class = PageNumberPaginationManual
#
#     def get(self, request):
#         #5、使用get_queryset获取查询集
#         project_qs = self.get_queryset()
#         #使用filter_queryset方法过滤查询集
#         project_qs=self.filter_queryset(project_qs)
#
#         #是用paginate_queryset来进行分页，然后返回分页之后的查询集
#         page=self.paginate_queryset(project_qs)
#         if page is not None:
#             serializer = self.get_serializer(instance=page, many=True)
#             #可以get_paginated_response方法返回
#             return self.get_paginated_response(serializer.data)
#
#
#         # 如果返回的是列表数据（多条数据）时，那么需要添加many=True这个参数
#         serializer = self.get_serializer(instance=project_qs, many=True)
#
#         #  JsonResponse第一个参数默认只能为dict字典,如果设为其他类型，需要将safe=False
#         return Response(serializer.data)
#
#     def post(self, request):
#         '''新增项目'''
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data, encoding='utf-8')
#
#         serializer = ProjectModelSerializer(data=python_data)
#
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return JsonResponse(serializer.errors)
#
#         serializer.save()
#
#         # 3、将模型类对象转化为字典然后返回
#         # 序列化过程
#
#         return JsonResponse(serializer.data, status=201)
#
#
# # 需要继承GenericAPIView基类
# class ProjectDetail(GenericAPIView):
#     # 2、必须指定queryset和serializer_class
#     # queryset用于指定需要使用的查询集
#     queryset = Projects.objects.all()
#     # serializer_class指定需要使用到的序列化器类
#     serializer_class = ProjectModelSerializer
#
#     # 使用lookup_field类属性，可以修改主路由名称
#     # lookup_field = 'id'
#
#     # def get_object(self, pk):
#     #     try:
#     #         return Projects.objects.get(id=pk)
#     #     except Projects.DoesNotExist:
#     #         raise Http404
#
#     def get(self, request, pk):
#
#         # 3、无需自定义get_object方法
#         # 使用get_object方法，返回详情视图所需的模型对象
#         project = self.get_object()
#         # serializer = ProjectSerializer(instance=project)
#         # 使用get_serializer获取序列化器类
#         serializer = self.get_serializer(instance=project)
#         # 如果前端请求头中未指定acceept，那么默认返回josn格式数据
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
#         # 2、获取ID为pk值的项目
#         project = self.get_object()
#
#         # 3、从前端获取json格式数据
#         json_data = request.body.decode('utf-8')
#         python_data = json.loads(json_data, encoding='utf-8')
#         serializer = self.get_serializer(instance=project, data=python_data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return Response(serializer.errors)
#         # 4、更新项目
#
#         # 在创建序列化器对象时，如果同时给instance和data传参
#         # 那么调用save（）方法，会自动化调用序列化器对象的updata方法
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
#         # 2、获取ID为pk值的项目
#         project = self.get_object()
#         project.delete()
#         return Response(None, safe=False, status=204)


# import json
# from django.http import HttpResponse, JsonResponse, Http404
# from django.views import View
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status, filters
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import mixins
#  from rest_framework import generics
#
# from projects.serializer import ProjectSerializer, ProjectModelSerializer
#
# from projects.models import Projects
# from utils.pagination import PageNumberPaginationManual
#
#
# # 1、首先继承mixins，然后继承GenericAPIView
# class ProjectsList(generics.ListCreateAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectModelSerializer
#
#     ordering_fields = ['name', 'leader']
#     filterset_fields = ['name', 'leader', 'tester']
#
#
# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectModelSerializer

import json
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from projects.serializer import ProjectSerializer, ProjectModelSerializer

from projects.models import Projects
from utils.pagination import PageNumberPaginationManual


# 1、首先继承mixins，然后继承GenericAPIView
#viewsets不再支持get 、post、put、delete等请求方法、二只支持action动作
#但是ViewSet未提供get_object、get_serializer等方法
#所以需要继承GenericViewSet
class ProjectViewSet(viewsets.GenericViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name', 'leader']
    filterset_fields = ['name', 'leader', 'tester']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

