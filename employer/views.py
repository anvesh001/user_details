from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
    #UserProfileForm

from django.contrib.auth.views import login
from django.contrib.auth import authenticate
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, EditProfileForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            post=form.save()

            #data=form.cleaned_data['']

            #user.experince=form.cleaned_data.get('experince')
            #user.phone=form.cleaned_data.get('phone')
            #user.price=form.cleaned_data.get('price')
            #user.save()
            username=form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
              for msg in form.error_messages:
                 messages.error(request, f'{msg}:{form.error_messages[msg]}')

    form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})


'''
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        emp_form=UserProfileForm(request.POST)

        if emp_form.is_valid() and user_form.is_valid():
            user=user_form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            employee = emp_form.save(commit=False)
            employee.user = user
            employee.save()

            return redirect('home')
    else:
        user_form = UserCreationForm()
        emp_form=UserProfileForm()
    return render(request, 'signup.html', { 'user_form':user_form,'emp_form':emp_form})
'''



def view_profile(request):
    employee=UserProfile.objects.all()
    args = {'employee':employee}
    return render(request, 'accounts/profile.html', args)





def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:

        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile2')
        else:
            return redirect('/accounts/changepassword')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
