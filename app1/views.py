from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Expense, Tag
from .forms import ExpenseForm, TagForm

# Index view to check if the app is working
def index(request):
    return HttpResponse("The app is working!   Check Urls for Review  ")

# View to handle expense creation
def create_expense(request):
  form = ExpenseForm() # Create instance of ExpenseForm Class
  if request.method == 'POST': 
    # Creats instance but this time its initialize with the data submited from the users input in request.POSt dict.
    form = ExpenseForm(request.POST)
    print(request.POST)

    if form.is_valid(): # Check if form is valid
    #   print(form.cleaned_data['tags'])  # Print the submitted value for tags 
      form.save()  # Save the form data
      print("save")
      return redirect('expense_list') # redirects the user to another view function named expense_list 
    
    else:
      # Form is not valid, handle form errors
      print("Form validation errors:")
      for field, error in form.errors.items():
        print(f"{field}: {error}")  # Print each error message
  else:
        form = ExpenseForm() # if request is not POST then GET request to display the initial empty form.
        context = {'form': form}
  return render(request, 'add_expense.html', context)#{'form': form}) 
 
 


def update_expenses(request, sno):
    form = ExpenseForm()
    print("data")
    expense = ""
    expense = get_object_or_404(Expense, id=sno)
    # expense = Expense.objects.get(expense,id=sno)
    print(expense , expense.cost, expense.id)
    if request.method == "POST":
        # form = ""
        form = ExpenseForm(request.POST, instance=expense)#, instance=expense
        print("request.POST")
        print(request.POST)
        
        if form.is_valid():

            # Save the updated data to the database:
            form.save()
            print("formData")
            # Redirect to a new URL:
            return redirect('expense_list')
    else:
        # Initialize the form with existing expense data:
        form = ExpenseForm(instance=expense)
         
    return render(request, 'update.html',{'form': form} ) #return HttpResponse("update works")

def delete_record(request, sno):

    try:
        # Get the expense object to be deleted
        expense = Expense.objects.get(id=sno)

        # Delete the expense object
        expense.delete()
        print(expense,"Expense deleted  successfully!")  # Print for debugging 

        # Redirect to the expense list page after successful deletion
        return redirect('expense_list')

    except Expense.DoesNotExist:
        # Handle case where expense with the given ID doesn't exist
        print("Expense not found!")  # Print for debugging 
        
    return redirect('expense_list')  # Redirect even if exception occurs 


# View to display the list of expenses
def expense_list(request):
    tags = Tag.objects.all()  # Get all tags (for filter dropdown)
    expenses = Expense.objects.all()
    # Check if a tag is selected in the filter
    selected_tag_id = request.GET.get('tag', None)
    if selected_tag_id:
        expenses = expenses.filter(tags__id=selected_tag_id)  # Filter by tag ID

    context = {'tags': tags, 'expenses': expenses}
    return render(request, 'expense_list.html', context)

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

 # This function handles a request for a tag report based on the provided tag ID.
def tag_report(request, tag_id):
 
    try:
        selected_tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        print("Tag Doesnt exist")
        # Handle  where the tag ID is invalid (tag doesn't exist)
        
        return render(request,  {'message': 'Invalid Tag ID'})

    # 2. Fetch Related Expenses:
    related_expenses = selected_tag.expenses.all()

    # 3. Prepare Context for Template:
    context = {
        'tag': selected_tag,  # The selected tag object
        'expenses': related_expenses,  # List of associated expense objects
    }

    # 4. Render the Template:
    return render(request, 'tag_expense.html', context)
