"""
=================
Author:delpan
Time:2021/3/18,0018
=================
"""
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    #前端传页数key为P
    page_query_param = 'p'
    #默认情况下，每一页显示的条数为2
    page_size = 2

