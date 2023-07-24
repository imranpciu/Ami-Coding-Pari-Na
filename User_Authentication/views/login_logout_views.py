from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout

def LoginPage(request):
    # Initialize the error message variable
    error_message = None 

    if request.method == 'POST':
        # Retrieve username and password from the POST data
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        # Authenticate the user using the provided credentials
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            # If the user is authenticated, log them in and redirect to the 'khoj_search' page
            login(request, user)
            return redirect('khoj_search')
        else:
            # If the user is not authenticated, set an error message
            error_message = "Username or Password is incorrect!!!"

    # Render the 'login.html' template with an optional error message
    return render(request, 'login.html', {'error_message': error_message})

def LogoutPage(request):
    logout(request)
    return redirect('login')
