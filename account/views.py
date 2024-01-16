from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import UserRegistrationForm, UserUpdateForm, StyledPasswordChangeForm
from .models import UserAccount
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect


class UserAccountCreateView(FormView):
    template_name = "user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        messages.success(self.request, "Register Successfully!! Welcome!!")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "user_login.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Login Successfully, Welcome Back!!")
        return super().form_valid(form)


# class UserLogoutView(LogoutView):
#     def get(self, request, *args, **kwargs):
#         logout(self.request)
#         messages.warning(self.request, "Logout Successfully!!")
#         return HttpResponseRedirect(reverse_lazy("home"))


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy("home")


class UserAccountUpdateView(View):
    template_name = "profile.html"

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
        return render(request, self.template_name, {"form": form})


class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = "password_change.html"
    form_class = StyledPasswordChangeForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, "Change Password Successfully!! Thank You!!")
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user

        return kwargs
