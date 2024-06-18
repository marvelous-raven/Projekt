from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterUserForm, ModifySuccessForm
from django.views import generic
from django.urls import reverse_lazy
from mainapp.models import UserProfile


class UserEditView(generic.UpdateView):
  form_class = ModifySuccessForm
  template_name = 'authentication/edit_profile.html'
  success_url = reverse_lazy('profile')

  def get_object(self):
    return self.request.user

def login_user(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')

    else:
      messages.success(request,
                       ("There was an error logging in. Please try again."))
      return redirect('login')

  else:
    return render(request, 'authentication/login.html', {})


def logout_user(request):
  logout(request)
  messages.success(request, ("You were logged out successfully!"))
  return redirect('home')


def register_user(request):
  if request.method == "POST":
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, "You were registered successfully!")
      return redirect('home')
  else:
    form = RegisterUserForm()

  return render(request, 'authentication/register.html', {'form': form})
