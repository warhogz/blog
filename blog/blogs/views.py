from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.detail import DetailView


class CustomLoginView(LoginView):
    template_name = 'blogs/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


class RegisterPage(FormView):
    template_name = 'blogs/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super(RegisterPage, self).get(*args, **kwargs)


class BlogList(LoginRequiredMixin, ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user=self.request.user)
        #  context['count'] = context['posts'].filter(complete=False).count()
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = '__all__'
    success_url = reverse_lazy('posts')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('posts')


class PostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'context', 'date_added']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "blogs/post.html"
