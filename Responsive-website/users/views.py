from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordResetView

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

##########activate##############
def activate(request, uidb64, token):
    User = CustomUser
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('registration_success')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('registration_success')

###########activate email################

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

##########Registration##################

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user = authenticate(email=email, password=password)
            # login(request, user)
            # messages.success(request, ('Youre now registered'))
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

################Registration Success####################

def registration_success(request):
    return render(request,'login.html')

# def c_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         CustomUser = authenticate(request, email=email, password=password)
#         if CustomUser is not None:
#             login(request, CustomUser)
#             # Redirect to a success page or home page
#             return redirect('success')  # Replace 'home' with your desired URL name
#         else:
#             # Invalid login
#             messages.error(request, 'Invalid email or password.')
#     return render(request, 'login.html')

#################Login########################3

def c_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate against the CustomUser model
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the appropriate page after login
                return redirect('success')  # Change 'profile' to your desired URL name
            else:
                for key, error in list(form.errors.items()):
                      if key == 'captcha' and error[0] == 'This field is required.':
                            messages.error(request, 'you must tick captcha to move forward for login')
                            continue
                # Handle invalid login credentials
                messages.error(request,('Error logging in'))
                return render(request, 'login.html', {'form': form})
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

########################Change Password#########################

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

# custom password change for before login itself #
# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm
#     template_name = 'forgot_password.html'
#     email_template_name = 'password_reset_email.html'
#     success_url = reverse_lazy('login')

###################Edit Profile#########################

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

################Logout#####################

def c_logout(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('demo')

##################Success##################

def success(request):
    return render(request, 'success.html')

############Terms#################

def terms(request):
      return render(request, 'terms.html')

##################Privacy###############

def privacy(request):
      return render(request, 'privacy.html')




