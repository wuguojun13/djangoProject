from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View


def index(request):
    '''
index视图
    :param request:
    :return:
    '''
    return HttpResponse('<h1> HEllo,soory</h1>')


class IndexView(View):
    """
    index主页类视图
    """

    def get(self,request):
        return HttpResponse('<h1> HEllo,soory</h1>')