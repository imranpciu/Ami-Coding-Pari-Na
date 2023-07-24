from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import KhojInputValue

@login_required(login_url='login')
def khoj_search(request):
    if request.method == 'POST':
        input_values = request.POST.get('input_values')
        search_value = request.POST.get('search_value')

        # Store the input values in the database
        input_values_list = [int(num.strip()) for num in input_values.split(",")]
        input_values_list.sort(reverse=True)
        input_values_str = ", ".join(str(num) for num in input_values_list)

        khoj_input = KhojInputValue(user=request.user, input_values=input_values_str)
        khoj_input.save()

        # Check if the search value is in the input values
        search_value_int = int(search_value)
        is_present = search_value_int in input_values_list

        return render(request, 'khoj_search.html', {'is_present': is_present})
    return render (request,'khoj_search.html')