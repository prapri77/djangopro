from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser


# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "register.html"

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            CustomUser = authenticate(email=email, password=password)
            login(request, CustomUser)
            messages.success(request, ('Youre now registered'))
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request,'login.html')

def c_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        CustomUser = authenticate(request, email=email, password=password)
        if CustomUser is not None:
            login(request, CustomUser)
            # Redirect to a success page or home page
            return redirect('success')  # Replace 'home' with your desired URL name
        else:
            # Invalid login
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')


def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('registration_success')
	else: 		#passes in user information
		form = PasswordChangeForm(user= request.user)

	context = {'form': form}
	return render(request, 'forgot_password.html', context)


def edit_profile(request):
	if request.method =='POST':
		form = CustomUserChangeForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('success')
	else: 		#passes in user information
		form = CustomUserChangeForm(instance= request.user)

	context = {'form': form}
	return render(request, 'edit_profile.html', context)

def c_logout(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('success')


def success(request):
    return render(request, 'success.html')




