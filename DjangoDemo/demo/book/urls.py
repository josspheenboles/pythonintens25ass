from django.urls import path
from .views import *
urlpatterns=[
path('',book_list,name='Blist'),
    path('New/',book_new,name='Bnew'),
    path('NewClass/',Book_New.as_view(),name='Bnewc'),
    path('NewForm/',book_newform,name='Bnewform'),
    path('NewFormModel/',book_newformmodel,name='Bnewformmodel'),
    path('Update/<int:id>',book_update,name='Bupdate'),
    path('UpdateClass/<int:id>',Book_update.as_view(),name='Bupdatec'),
    path('UpdateForm/<int:id>',book_updateform,name='Bupdateform'),
    path('UpdateFormModel/<int:id>',book_updateformmodel,name='Bupdateformmodel'),
    path('Delete/<int:id>',book_delete,name='Bdelete'),
    path('DeleteClass/<int:id>',book_deleteclass.as_view(),name='Bdeletec'),
    path('<int:id>',book_show,name='Bshow'),
]