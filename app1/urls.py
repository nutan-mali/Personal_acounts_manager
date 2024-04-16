from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("expense_list/", views.expense_list, name="expense_list"),
#     path("invoice/<int:invoice_id>/", views.invoice_detail, name="invoice_detail"),
]