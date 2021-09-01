from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from accounts.form import CreateUserForm


class RegisterUser(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'formregister.html', {'form':form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        return render(request, 'formregister.html', {'form': form})