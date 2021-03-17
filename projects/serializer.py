"""
=================
Author:delpan
Time:2021/3/15,0015
=================
"""

from rest_framework import serializers

# 1、继承serializer类或者子类
from rest_framework.validators import UniqueValidator

from projects.models import Projects


# 创建自定义校验器
# 第一个参数为字段的值
def is_unique_project_name(name):
    if '项目' not in name:
        raise serializers.ValidationError('项目名称中必须包含"项目"')


class ProjectSerializer(serializers.Serializer):
    '''
    创建项目序列化器类
    '''
    # 1、序列化器中定义的类属性字段与模型类字段一一对应
    # 2.label选项相当于verbose_name,help_text
    # 3、定义的序列化器字段，默认既可以进行序列化输出，也可以进行反序列化输入
    # 4、read_only=True,指定该字段只能进行序列化输出，不进行反序列化
    # 5、write_only=True，指定该字段只能进行反序列化输入，但不能进行序列化输出
    # 6、需要哪些字段，那么在序列化器中就定义哪些字段

    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='项目名称', max_length=200,
                                 help_text='项目名称', write_only=True,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名不能重复'),
                                             is_unique_project_name])
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    # allow_null相当于模型类中的null，allow_blank相当于模型类中的blank
    desc = serializers.CharField(label='简要描述', allow_null=True, allow_blank=True, default='')


    #单字段校验
    #字段定义的限制（包含validators列表条目从左到右进行校验）--》单字段校验（validators_字段名）-->duo'z
    #单字段的校验器，validate_字段名开头
    def validate_name(self, value):
        if not value.endwith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        #当校验成功之后，一定要返回value
        return value


    def validate(self, attrs):
        '''
        多字段联合校验
        :param attrs:
        :return:
        '''
        if 'icon'not in attrs['tester'] and 'icon' not in attrs['leader']:
            raise serializers.ValidationError('icon必须是项目负责人或者是项目测试人员')
        return attrs


    def create(self, validated_data):
        #project = Projects.objects.create(**validated_data)
        return Projects.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()

        return instance