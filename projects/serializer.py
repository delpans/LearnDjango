"""
=================
Author:delpan
Time:2021/3/15,0015
=================
"""

from rest_framework.serializers import ModelSerializer
from projects.models import Projects


class ProjectsModelSerializer(ModelSerializer):
    class Meta:
        model=Projects
        fields="__all__"
