from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from . import forms

class UserCreateView(generic.CreateView):
    model = User
    form_class = forms.CustomUserCreationForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('login')
