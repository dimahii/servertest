from django.urls import path
from . import views

app_name = 'mana'
urlpatterns=[
    path('add/',views.add,name='add'),
    path('accept/',views.accept,name='accept'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('',views.index,name='index'),
    path('edit',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
]
