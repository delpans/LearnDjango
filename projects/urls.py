"""
=================
Author:delpan
Time:2021/3/4,0004
=================z
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from projects import views

# 1、每一个应用（模块）都会维护一个子路由（当前应用的路由信息）
# 2、跟主路由一样，也是从上到下匹配
# 3、能够匹配上。则执行path第二个参数指定的视图，匹配不上抛404异常


router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
urlpatterns = [
    # path('index/', index)
    # 如果为类视图，path第二个参数为类视图名.as_view()
    # path('',views.IndexView.as_view()),

    # int未路径参数类型转化器
    # ：冒号左边为转化器，右边为参数别名
    # int、slug、uuid、
    # path('<int:pk>/',views.IndexView.as_view())
    path('projects/', views.ProjectsList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]

urlpatterns += router.urls
