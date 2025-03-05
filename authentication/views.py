from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')



class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

