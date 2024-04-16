from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("expense_list/", views.expense_list, name="expense_list"),
    path("add_expense/", views.create_expense, name="create_expense"),
    path("tag_list/", views.tag_list, name="tag_list"),
    path("add_tag/", views.create_tag, name="create_tag"),
     path('delete/<int:id>',views.Delete_record,name='delete'),
]