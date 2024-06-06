from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Book
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import Q


def home(request):
    return render(request, "library/index.html")

class SignUpPage(CreateView):
    template_name = 'library/user_form.html'
    model = User
    form_class = CustomUserCreationForm

class ListPage(generic.ListView):
    template_name = "library/booklist.html"
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') != None else ""
        p = int(self.request.GET.get('p')) if self.request.GET.get('p') != None else self.paginate_by
        self.paginate_by = p
        # self.set_pagination()
        book_list = Book.objects.filter(
            Q(title__icontains = q) |
            Q(author_surname__icontains = q) |
            Q(genre__icontains = q) |
            Q(publisher__icontains = q)
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
        "borrowed",
    ]

class EditPage(UpdateView):
    model = Book
    fields = [
        "title",
        "author_name",
        "author_surname",
        "publisher",
        "genre",
        "borrowed",
    ]

class DeletePage(DeleteView):
    model = Book
    success_url = reverse_lazy("library:ListPage")