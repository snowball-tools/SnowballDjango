from django.shortcuts import get_object_or_404, render
import markdown
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


def documentation_detail(request, pk):
    documentation = get_object_or_404(Documentation, pk=pk)
    documentation.content = markdown.markdown(documentation.content)
    return render(
        request,
        "snowball_documentation/documentation_detail.html",
        {"documentation": documentation},
    )
