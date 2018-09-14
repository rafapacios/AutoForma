from django.conf.urls import *
from catalogo.views import catalogo

urlpatterns = [

    url(r'^catalogo/$', catalogo, name='catalogo')

]