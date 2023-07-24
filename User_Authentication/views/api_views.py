# User_Authentication/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import KhojInputValue
import datetime

@csrf_exempt
def get_all_input_values(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        start_datetime = request.POST.get('start_datetime')
        end_datetime = request.POST.get('end_datetime')

        try:
            user_id = int(user_id)
            start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S.%f')
            end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S.%f')

            khoj_input_values = KhojInputValue.objects.filter(
                user_id=user_id,
                timestamp__range=(start_datetime, end_datetime)
            ).order_by('-timestamp')

            payload = []
            for khoj_input in khoj_input_values:
                payload.append({
                    'timestamp': khoj_input.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'input_values': khoj_input.input_values,
                })

            response = {
                'status': 'success',
                'user_id': user_id,
                'payload': payload,
            }
            return JsonResponse(response)
        except (ValueError, TypeError, KhojInputValue.DoesNotExist) as e:
            response = {
                'status': 'error',
                'message': str(e),
            }
            return JsonResponse(response, status=400)

    response = {
        'status': 'error',
        'message': 'Invalid request method. Use POST to get input values.',
    }
    return JsonResponse(response, status=405)
