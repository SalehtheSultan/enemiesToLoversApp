# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage

# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

def login_register_view(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            # Handle registration form submission
            form = UserRegistrationForm(request.POST)
            login_form = AuthenticationForm()
            if form.is_valid():
                # Registration logic...
                messages.success(request, 'Please confirm your email address to complete the registration.')
                return redirect('accounts:login')
        elif 'signin' in request.POST:
            # Handle login form submission
            form = UserRegistrationForm()
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('profiles:profile_view')
    else:
        form = UserRegistrationForm()
        login_form = AuthenticationForm()
    return render(request, 'accounts/register.html', {'form': form, 'login_form': login_form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email confirmed
            user.save()
            # Send activation email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(request, 'Please confirm your email address to complete the registration.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
        login_form = AuthenticationForm()
    return render(request, 'accounts/register.html', {'form': form, 'login_form': login_form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been activated successfully.')
        return redirect('profiles:profile_view')
    else:
        return HttpResponse('Activation link is invalid!')
