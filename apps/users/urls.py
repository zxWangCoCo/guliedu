"""GuliEdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import user_register,user_login,user_logout,user_active,user_info,user_change_image
app_name = 'users'
urlpatterns = [
    url(r'^user_register/$',user_register,name="user_register"),#注册url
    url(r'^user_login/$',user_login,name='user_login'),
    url(r'^user_logout/$',user_logout,name='user_logout'),
    url(r'^user_active/(\w+)/$',user_active,name='user_active'), # (\w+)捕获传递的参数
    url(r'^user_info/$',user_info,name='user_info'),
    url(r'^user_change_image/$',user_change_image,name='user_change_image'),
]
