from django.shortcuts import render,HttpResponse
from .models import Expense
from .forms import ExpenseForm
# Create your views here.
def index(request):
    return HttpResponse("works")
    
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})
def create_expense(request):
    return render(request, 'add_expense.html')

def tag_list(request):
    return render(request, 'tag_list.html')

def create_tag(request):
     return render(request, 'create_tag.html')