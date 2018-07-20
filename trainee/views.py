from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomTrainee


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def settings(request):
    user = request.user
    person=CustomTrainee.objects.filter(username=user)
    return render(request,'setting.html', {'p':person})