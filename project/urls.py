
from django.urls import path
from project.views import index
from project import views
urlpatterns = [
    # path('index/',index)
    #如果为类视图path第二个参数
    path('',views.IndexView.as_view())
]
