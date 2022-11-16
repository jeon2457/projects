
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views  # mysite\pybo\views\base_views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),  # 로그인/로그아웃 하기위해서 사용!
    path('', base_views.index, name='index'),   # '/' 에 해당되는 path
]
