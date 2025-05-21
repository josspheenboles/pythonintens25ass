from django.urls import path,include
from .views import *
from .api.views import *
urlpatterns=[
    #api function based
    path('API/',getall,name='apiall'),
    path('API/<int:id>',getbyid,name='getbyid'),
    # class Based
    path('CAPI/',BookClass.as_view(),name='BookClass'),
    path('CAPI/<int:id>',BookClass2.as_view(),name='BookClassbyid'),
    # generic class Based
    path('GAPI/',BookList.as_view()),




    path('',book_list,name='Blist'),
    path('ListClass',book_list_class.as_view(),name='Blistc'),
    path('ListClassG',Book_list_classG.as_view(),name='BlistcG'),
    path('NewG/',Book_newG.as_view(),name='BnewG'),
    path('New/',book_new,name='Bnew'),
    path('NewClass/',Book_New.as_view(),name='Bnewc'),
    path('NewForm/',book_newform,name='Bnewform'),
    path('NewFormModel/',book_newformmodel,name='Bnewformmodel'),
    path('Update/<int:id>',book_update,name='Bupdate'),
    path('UpdateClass/<int:id>',Book_update.as_view(),name='Bupdatec'),
    path('UpdateClassG/<int:pk>',Book_updateG.as_view(),name='BupdatecG'),
    path('UpdateForm/<int:id>',book_updateform,name='Bupdateform'),
    path('UpdateFormModel/<int:id>',book_updateformmodel,name='Bupdateformmodel'),
    path('Delete/<int:id>',book_delete,name='Bdelete'),
    path('DeleteClass/<int:id>',book_deleteclass.as_view(),name='Bdeletec'),
    path('DeleteClassG/<int:pk>',Book_deleteclassG.as_view(),name='BdeletecG'),
    path('<int:id>',book_show,name='Bshow'),
]