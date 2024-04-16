from django.shortcuts import render,HttpResponse,redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.
def index(request):
    return HttpResponse("works")
    
def create_expense(request):
    form=ExpenseForm()
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        form.save()
        form=ExpenseForm()
    # return redirect('expense_list')
    data=Expense.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request, 'add_expense.html', context)


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def create_tag(request):
     return render(request, 'create_tag.html')

def tag_list(request):
    return render(request, 'tag_list.html')
