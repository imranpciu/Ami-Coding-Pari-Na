from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import KhojInputValue
from django.utils import timezone

@csrf_exempt
def get_all_input_values(request):
    if request.method == 'POST':
        # Retrieve input parameters from the POST request
        user_id = int(request.POST.get('user_id'))
        start_datetime = timezone.datetime.strptime(request.POST.get('start_datetime'), '%Y-%m-%d %H:%M:%S').astimezone(timezone.pytz.timezone('Asia/Dhaka'))
        end_datetime = timezone.datetime.strptime(request.POST.get('end_datetime'), '%Y-%m-%d %H:%M:%S').astimezone(timezone.pytz.timezone('Asia/Dhaka'))

        try:
            # Retrieve input values from the database within the specified time range
            khoj_input_values = KhojInputValue.objects.filter(
                user_id=user_id,
                timestamp__range=(start_datetime, end_datetime)
            ).order_by('-timestamp')

            # Create payload containing input values and timestamps
            payload = []
            for khoj_input in khoj_input_values:
                payload.append({
                    'timestamp': khoj_input.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'input_values': khoj_input.input_values,
                })

            # Construct JSON response
            response = {
                'status': 'success',
                'user_id': user_id,
                'payload': payload,
            }
            return JsonResponse(response)
        except KhojInputValue.DoesNotExist as e:
            # Handle case where no input values are found within the time range
            response = {
                'status': 'error',
                'message': str(e),
            }
            return JsonResponse(response, status=400)

    # Handle invalid request method (only POST is allowed)
    response = {
        'status': 'error',
        'message': 'Invalid request method. Use POST to get input values.',
    }
    return JsonResponse(response, status=405)