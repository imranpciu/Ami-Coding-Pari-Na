from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import KhojInputValue
from django.utils import timezone

@login_required(login_url='login')
def khoj_search(request):
    if request.method == 'POST':
        # Retrieve input values and search value from the POST data
        input_values = request.POST.get('input_values')
        search_value = request.POST.get('search_value')

        # Store the input values in the database
        input_values_list = [int(num.strip()) for num in input_values.split(",")]
        input_values_list.sort(reverse=True)
        input_values_str = ", ".join(str(num) for num in input_values_list)

        # Create the KhojInputValue object and set the timestamp with the current datetime
        khoj_input = KhojInputValue(user=request.user, input_values=input_values_str, timestamp=timezone.now())
        khoj_input.save()

        # Check if the search value is in the input values
        search_value_int = int(search_value)
        is_present = search_value_int in input_values_list

        return render(request, 'khoj_search.html', {'is_present': is_present})
    else:
        # If the request method is GET, render the 'khoj_search.html' template with the search form
        return render(request, 'khoj_search.html')
