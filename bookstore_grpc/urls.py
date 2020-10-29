"""bookstore_grpc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from book.handlers import \
    category_grpc_handlers, \
    publisher_grpc_handlers, \
    author_grpc_handlers, \
    book_grpc_handlers


urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    category_grpc_handlers(server)
    publisher_grpc_handlers(server)
    author_grpc_handlers(server)
    book_grpc_handlers(server)
