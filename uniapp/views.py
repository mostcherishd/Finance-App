from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,MyForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account has been created ' + user)
                return redirect('login_user')
        
        context = {'form':form}
        return render(request, 'register_user.html',context)

 
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashbase')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashbase')
            else:
                messages.info(request, 'username or password is incorrect')


        context = {}
        return render(request, 'login_user.html', context)


# sending Email function
def send_email_view(request):
    if request.method == 'POST':
        subject = 'Subject of the email'
        message = 'Body of the email'
        recipient_list = ['abu.adams120@gmail.com']
        sender_email = settings.EMAIL_HOST_USER
        
        send_mail(subject, message, sender_email, recipient_list)
        
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('index')

def home(request):
    pass

def main_base(request):
    return render(request, 'main_base.html', {})
def index(request):
    return render(request, 'index.html', {})
@login_required(login_url='login_user')  
def dashboard(request):
    return render(request, 'dashboard.html', {})
@login_required(login_url='login_user')
def transaction(request):
    return render(request, 'transaction.html', {})
@login_required(login_url='login_user')
def invest_history(request):
    return render(request, 'invest_history.html', {})
@login_required(login_url='login_user')
def invest_plan(request):
    return render(request, 'invest_plan.html', {})

@login_required(login_url='login_user')
def create_deposit(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_deposit')
    else:
        form = MyForm()
    return render(request,'create_deposit.html',{'form':form})


@login_required(login_url='login_user')
def deposit_history(request):
    return render(request, 'deposit_history.html', {})
@login_required(login_url='login_user')
def payout(request):
    return render(request, 'payout.html', {})
@login_required(login_url='login_user')
def dashbase(request):
    return render(request, 'dashbase.html', {})
@login_required(login_url='login_user')
def main_dash(request):
    return render(request, 'main_dash.html', {})




# sending email function


    


