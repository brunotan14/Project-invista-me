"""
URL configuration for investimento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from investimentoapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.investimentos, name='investimentos'),
    path('novo_investimento/<int:id_investimento>',views.editar, name='editar'),
    path('minhapagina/',views.minhapagina, name='minhapagina'),
    path('novo_investimento/',views.criar,name='novo_investimento'),
    path('<int:id_investimento>/',views.detalhe, name='detalhe'),
    path('excluir_investimento/<int:id_investimento>',views.excluir, name='excluir'),
    
]

# <int: id_investimento>: É o nome da variável que será passada para a view como um argumento. O valor do inteiro capturado na URL será atribuído a essa variável.
# Por exemplo, se a URL acessada for http://localhost:8000/5/, o Django capturará 5 como o id_investimento e o passará como argumento para a view.