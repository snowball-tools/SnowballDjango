from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Documentation


class DocumentationListView(ListView):
    model = Documentation
    template_name = "documentation_list.html"


class DocumentationDetailView(DetailView):
    model = Documentation
    template_name = "documentation_detail.html"


class DocumentationCreateView(CreateView):
    model = Documentation
    template_name = "documentation_form.html"
    fields = ["component", "technology", "content"]


class DocumentationUpdateView(UpdateView):
    model = Documentation
    template_name = "documentation_form.html"
    fields = ["component", "technology", "content"]


class DocumentationDeleteView(DeleteView):
    model = Documentation
    template_name = "documentation_confirm_delete.html"
    success_url = "/"
