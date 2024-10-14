"""
URL configuration for webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from webapp.views import home,save_data,delete_todo,edit_todolist,update_todolist

urlpatterns = [
    path('',home),
    path('save_data/',save_data),
    path('delete_todo/',delete_todo),
    path('edit_todolist/',edit_todolist),
    path('update_todolist/',update_todolist),

    path('admin/', admin.site.urls),
]
