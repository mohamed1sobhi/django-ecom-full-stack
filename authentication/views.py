from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from cartAndCheckout.models import Cart

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        Cart.objects.get_or_create(user=user, defaults={'total': 0})
        return response



class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

