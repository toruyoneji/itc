from django.urls import path
from .views import NippoListView, NippoDetailView, NippoCreateFormView, NippoUpdateView, NippoDeleteView


urlpatterns = [
    path("", NippoListView.as_view(), name="nippo-list"),
    path("detail/<int:pk>", NippoDetailView.as_view(), name="nippo-detail"),
    path("create/", NippoCreateFormView.as_view(), name="nippo-create"),
    path("update/<int:pk>", NippoUpdateView.as_view(), name="nippo-update"),
    path("delete/<int:pk>", NippoDeleteView.as_view(), name="nippo-delete"),
]