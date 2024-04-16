from django.shortcuts import render,HttpResponse,redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.
def index(request):
    return HttpResponse("works")
    
def create_expense(request):
  form = ExpenseForm()
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    print(request.POST)
    if form.is_valid(): # Check if form is valid
      print(form.cleaned_data['tags'])  # Print the submitted value for tags 
      form.save()  # Save the form data
      print("save")
      return redirect('expense_list')  
    else:
      # Form is not valid, handle form errors
      print("Form validation errors:")
      for field, error in form.errors.items():
        print(f"{field}: {error}")  # Print each error message
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
