from django.urls import path
from .views import *
urlpatterns=[
path('',book_list,name='Blist'),
    path('New/',book_new,name='Bnew'),
    path('NewForm/',book_newform,name='Bnewform'),
    path('Update/<int:id>',book_update,name='Bupdate'),
    path('Delete/<int:id>',book_delete,name='Bdelete'),
    path('<int:id>',book_show,name='Bshow'),
]