from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login')) 
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_index'))

# Once user is logged in redirect to homepage
def show_index(request):
    print(request.user.username)
    return redirect('quiz:index')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('quiz:index')

def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("quiz:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="authentication/register.html", context={"register_form":form})