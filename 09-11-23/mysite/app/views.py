from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, UserRegistionForm
from django.contrib.auth.models import User
from datetime import datetime
from .models import daliytime
# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, "home.html")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home page
                print("sucess")
                return redirect("profile")
            print("your password is wrong try to login")
        return render(request, "login.html", {"form": form})


# class RegistionView(View):
# form_class = UserRegistionForm

# def get(self, request):
#     return render(request, "registration.html", {"form": self.form_class})

# def post(self, request):
#     form_data = self.form_class(request.POST)

#     if form_data.is_valid():
#         print(form_data.cleaned_data)
#     else:
#         context = {"form": self.form_class, "error": form_data.errors}
#         return render(request, "registration.html", context)



class RegistrationView(View):
    def get(self, request):
        form = UserRegistionForm()
        return render(request, "registration.html", {"form": form})

    def post(self, request):
        form = UserRegistionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(username=first_name,first_name=first_name, last_name=last_name, email=email,password=password)
            user.save()
            login(request, user)

            return redirect("profile")  # Redirect to the user's profile or another page
        return render(request, "registration/register.html", {"form": form})

# class StarTime(View):
#     def get(self,request):
#         user =  request.user
#         start_time = datetime.now()
#         # end_time = datetime.now() 
#         t = daliytime(starttime = start_time)
#         t.save()
#             # return redirect("home") 
#         return redirect("home")


