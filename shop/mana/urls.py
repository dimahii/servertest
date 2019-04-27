from django.urls import path
from . import views

app_name = 'mana'
urlpatterns=[
    path('add/',views.add,name='add'),
    path('accept/',views.accept,name='accept')
]
