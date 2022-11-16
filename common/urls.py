from django.urls import path
from django.contrib.auth import views as auth_views  # 인증관련
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # {% url 'common:logout' %}에 대응하는 URL 매핑
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # 회원가입
]
