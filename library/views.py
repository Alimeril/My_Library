from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Book
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.db.models import Q


class Home(generic.TemplateView):
    template_name = "library/index.html"

class SignUpPage(CreateView):
    template_name = 'library/user_form.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("library:UserCreateConfirm")
    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            form.add_error('username', f'Username "{username}" is already in use.')
            return self.form_invalid(form)
        elif User.objects.filter(email=email).exists():
            form.add_error('email', f'Email "{email}" is already in use.')
            return self.form_invalid(form)
        
class LoginPage(LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'library/login_form.html'
    next_page = 'library:home'

class ConfirmLogout(generic.TemplateView):
    template_name = 'library/logout_form.html'

class LogoutPage(LogoutView):
    model = User
    template_name = 'library/logout_form.html'
    # next_page = 'library:home'

def user_confirm(request):
    return render(request,'library/user_creation_confirm.html')

class ListPage(LoginRequiredMixin, generic.ListView):
    template_name = "library/booklist.html"
    context_object_name = 'book_list'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') != None else ""
        p = int(self.request.GET.get('p')) if self.request.GET.get('p') != None else self.paginate_by
        self.paginate_by = p
        # self.set_pagination()
        book_list = Book.objects.filter(
            Q(user = self.request.user) & 
            (
                Q(title__icontains = q) |
                Q(author_surname__icontains = q) |
                Q(genre__icontains = q) |
                Q(publisher__icontains = q) |
                Q(description__icontains = q)        
            )
            
        ).values()
        return book_list
    
    def get_context_data(self, *args, **kwargs):
        context = super(ListPage,self).get_context_data(*args,**kwargs)
        q = self.request.GET.get('q') if self.request.GET.get('q') != None else ""
        p = int(self.request.GET.get('p')) if self.request.GET.get('p') != None else self.paginate_by
        context['query'] = q 
        context['pagination'] = p
        return context


class DetailView(generic.DetailView):
    model = Book
    template_name = "library/details.html"

class AddPage(CreateView):
    model = Book
    fields = [
        "title",
        "author_name",
        "author_surname",
        "publisher",
        "genre",
        "description",
        "borrowed",
    ]
    def form_valid(self, form: forms.BaseModelForm):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditPage(UpdateView):
    model = Book
    fields = [
        "title",
        "author_name",
        "author_surname",
        "publisher",
        "genre",
        "description",
        "borrowed",
    ]

class DeletePage(DeleteView):
    model = Book
    success_url = reverse_lazy("library:ListPage")