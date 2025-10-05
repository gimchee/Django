from django.urls import path
from . import views  # 현재 폴더(앱)에 있는 views.py를 가져옵니다.

urlpatterns = [
    # todos/ 로 접속했을 때 views.py의 index 함수를 실행합니다.
    path('', views.index, name='index'),
]