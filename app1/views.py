from django.shortcuts import render, HttpResponse, redirect
from .models import Expense, Tag
from .forms import ExpenseForm, TagForm

# Index view to check if the app is working
def index(request):
    return HttpResponse("The app is working!   Check Urls for Review")

# View to handle expense creation
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

def delete_record(request,id):
    a=Expense.objects.get(pk=id)
    a.delete()
    return redirect('expense_list')

# View to display the list of expenses
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

# View to create a new tag
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')  # Redirect to tag list page after successful creation
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})

# View to display the list of tags
def tag_list(request):
    tags = Tag.objects.all()  # Fetch all tags from the database
    return render(request, 'tag_list.html', {'tags': tags})

# View to display all expenses associated with a selected tag
# def tag_expenses(request, tag_id):
#     tag = Tag.objects.get(id=tag_id)
#     expenses = Expense.objects.filter(tags=tag)
#     return render(request, 'tag_expenses.html', {'tag': tag, 'expenses': expenses})