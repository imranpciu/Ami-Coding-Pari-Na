from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def SignupPage(request):
    error_message = None  # Initialize the error message variable

    if request.method == 'POST':
        # Retrieve username, email, password1, and password2 from the POST data
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            # If the passwords don't match, set an error message
            error_message = "Confirm password not match!!"

        else:
            # If the passwords match, create a new User object with the provided credentials and save it
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    # Render the 'signup.html' template with an optional error message
    return render(request, 'signup.html', {'error_message': error_message})
