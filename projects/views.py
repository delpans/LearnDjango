import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet


from projects.serializer import ProjectsModelSerializer

from projects.models import Projects




class ProjectsList(View):
    def get(self, request):
        # 1、从数据库中获取所有的项目信息
        project_qs = Projects.objects.all()

        # 2、将数据库模型实例转化为字典类型（嵌套字典的列表）
        project_list = []
        for project in project_qs:
            project_list.append(
                {
                    'name': project.name,
                    'leader': project.leader,
                    'tester': project.tester,
                    'programer': project.programer,
                    'publish_app': project.publish_app,
                    'desc': project.desc
                }
            )
        #  JsonResponse第一个参数默认只能为dict字典,如果设为其他类型，需要将safe=False
        return JsonResponse(project_list, safe=False)

    def post(self, request):
        '''新增项目'''
        # 1、从前端获取json格式数据，转化为python中的类型
        # 为了严谨性，这里需要做各种复杂的校验
        # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
        #反序列化过程
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        # 2、向数据库中新增项目
        # project = Projects.objects.create(name=python_data['name'],
        #                                       leader=python_data['leader'],
        #                                       tester=python_data['tester'],
        #                                       programer=python_data['programer'],
        #                                       publish_app=python_data['publish_app'],
        #                                       desc=python_data['desc'])

        project = Projects.objects.create(**python_data)

        # 3、将模型类对象转化为字典然后返回
        #序列化过程
        one_dict = {
            'name': project.name,
            'leader': project.leader,
            'tester': project.tester,
            'programer': project.programer,
            'publish_app': project.publish_app,
            'desc': project.desc
        }

        return JsonResponse(one_dict, status=201)


class ProjectDetail(View):
    def get(self, request, pk):
        # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
        # 省略
        # 2、获取指定pk值的项目
        project = Projects.objects.get(id=pk)

        # 3、将模型类对象转化为字典
        #序列化过程
        one_dict = {
            'name': project.name,
            'leader': project.leader,
            'tester': project.tester,
            'programer': project.programer,
            'publish_app': project.publish_app,
            'desc': project.desc
        }
        return JsonResponse(one_dict)

    def put(self, request, pk):
        # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
        # 2、获取ID为pk值的项目
        project = Projects.objects.get(id=pk)

        # 3、从前端获取json格式数据
        #反序列化
        # 为了严谨性，这里需要做各种复杂的校验
        # 比如：是否是json，传递的项目数据是否符合要求，有些必传参数是否携带
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        # 4、更新项目
        project.name = python_data['name']
        project.leader = python_data['leader']
        project.tester = python_data['tester']
        project.programer = python_data['programer']
        project.publish_app = python_data['publish_app']
        project.desc = python_data['desc']

        project.save()

        # 5、将模型类对象转化为字典
        #序列化
        one_dict = {
            'name': project.name,
            'leader': project.leader,
            'tester': project.tester,
            'programer': project.programer,
            'publish_app': project.publish_app,
            'desc': project.desc
        }
        return JsonResponse(one_dict, status=201)

    def delete(self, request, pk):
        # 1、校验前端传递的pk（项目id）值，类型是否正确（正整数），在数据库中是否存在
        # 2、获取ID为pk值的项目
        project = Projects.objects.get(id=pk)
        project.delete()
        return JsonResponse(None, safe=False, status=204)


class ProjectViewSet(ModelViewSet):
    queryset=Projects.objects.all()
    serializer_class = ProjectsModelSerializer