from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models.signals import post_save

from .models import CustomUser, Profile, File
from .forms import RegisterForm, LoginForm, FileForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('profile', new_user.id)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile', user.id)
                else:
                    return HttpResponse('Отключённая учётная запись')
            else:
                return HttpResponse('Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class ProfileView(DetailView):
	model = Profile
	template_name = 'users/profile.html'
	context_object_name = 'profile'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


class Files(ListView):
    model = File
    template_name = 'users/files.html'
    context_object_name = 'files'

    def get_queryset(self):
        return File.objects.filter(user=self.request.user)


def file(request, pk):
    file = File.objects.get(pk=pk)
    return render(request, 'users/file.html', {'file': file})


# class File(DetailView):
#     model = File
#     template_name = 'users/file.html'
#     context_object_name = 'file'


def add_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = request.FILES['file'].name
            form.user = request.user
            form.save()
            return redirect('files')
    else:
        form = FileForm()
    return render(request, 'users/add_file.html', {'form': form})


class FileUpdate(UpdateView):
    model = File
    template_name = 'users/file_update.html'

    fields = ['name', 'file']


class FileDelete(DeleteView):
    model = File
    success_url = '/users/files/'
    template_name = 'users/file_delete.html'