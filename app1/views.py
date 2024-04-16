from django.shortcuts import render,HttpResponse,redirect
from .models import Expense
from .forms import ExpenseForm
# Create your views here.
def index(request):
    return HttpResponse("works")
    
def create_expense(request):
    form = ExpenseForm()  # Initialize the form instance
    if request.method == 'POST':
        form = ExpenseForm(request.POST)  # Bind form with POST data
        print("Works ")
        if form.is_valid():  # Check if form is valid
            form.save()  # Save the form data
            # Optionally,  can add a success message here
            print("test")
            # Redirect to expense list after successful form submission
            return redirect('expense_list')  # Assuming 'expense_list' is the URL name for your expense list view
        else:
            # Form is not valid, handle form errors
            print("Form validation Error")  # Get form validation errors 
            return render(request, 'add_expense.html', {'form': form})
    # If request method is not POST (GET request), render the form
    return render(request, 'add_expense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def create_tag(request):
     return render(request, 'create_tag.html')

def tag_list(request):
    return render(request, 'tag_list.html')
