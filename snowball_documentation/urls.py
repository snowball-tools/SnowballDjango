from django.urls import path
from .views import (
    DocumentationListView,
    DocumentationDetailView,
    DocumentationCreateView,
    DocumentationUpdateView,
    DocumentationDeleteView,
)

app_name = "snowball_documentation"

urlpatterns = [
    path("", DocumentationListView.as_view(), name="documentation-list"),
    path("new/", DocumentationCreateView.as_view(), name="documentation-create"),
    path("<int:pk>/", DocumentationDetailView.as_view(), name="documentation-detail"),
    path(
        "<int:pk>/update/",
        DocumentationUpdateView.as_view(),
        name="documentation-update",
    ),
    path(
        "<int:pk>/delete/",
        DocumentationDeleteView.as_view(),
        name="documentation-delete",
    ),
]
