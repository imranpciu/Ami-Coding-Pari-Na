from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import KhojInputValue
from django.utils import timezone

@login_required(login_url='login')
def khoj_search(request):
    if request.method == 'POST':
        input_values = request.POST.get('input_values')
        search_value = request.POST.get('search_value')

        # Validate input_values
        input_values_list = [int(num.strip()) for num in input_values.split(",") if num.strip().isdigit()]
        
        # Check if input_values_list is empty or not
        if not input_values_list:
            error_message = "Invalid input values. Please enter a valid comma-separated list of integers."
            return render(request, 'khoj_search.html', {'error_message': error_message})

        input_values_list.sort(reverse=True)
        input_values_str = ", ".join(str(num) for num in input_values_list)

        # Create the KhojInputValue object and set the timestamp with the current datetime
        khoj_input = KhojInputValue(user=request.user, input_values=input_values_str, timestamp=timezone.now())
        khoj_input.save()

        # Check if the search value is in the input values
        search_value_int = int(search_value)
        is_present = search_value_int in input_values_list

        return render(request, 'khoj_search.html', {'is_present': is_present})
    return render(request, 'khoj_search.html')
