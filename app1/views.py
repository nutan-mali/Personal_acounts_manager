from django.shortcuts import render,HttpResponse,redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.
def index(request):
    return HttpResponse("works")
    
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print("Form is valid. Cleaned data:")
            print(form.cleaned_data)  # Print cleaned form data for debugging
            form.save()
            return redirect('expense_list')
        else:
            print("Form errors:")
            print(form.errors)  # Print form errors for debugging
            # Handle form errors
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

  

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def create_tag(request):
     return render(request, 'create_tag.html')

def tag_list(request):
    return render(request, 'tag_list.html')
