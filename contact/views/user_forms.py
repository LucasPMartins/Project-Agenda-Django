from django.shortcuts import render,redirect
from django.contrib import messages,auth
from contact.forms import RegisterForm,RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            auth.login(request, form.instance)
            return redirect('contact:index')

    return render(
        request, 'contact/register.html',
        {
            'form': form,
        }
        )

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            auth.login(request, form.instance)
            messages.success(request, 'User updated successfully')

    return render(request,'contact/user_update.html',{'form': form})

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('contact:index')

        messages.error(request, 'Invalid loggin credentials')

    return render(request,'contact/login.html',{'form': form,})

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'User logged out successfully')
    return redirect('contact:index')