from django.urls import path
from .views import NippoListView, NippoDetailView, NippoCreateFormView, nippoUpdateView, nippoDeleteView


urlpatterns = [
    path("", NippoListView.as_view(), name="nippo-list"),
    path("detail/<int:pk>", NippoDetailView.as_view(), name="nippo-detail"),
    path("create/", NippoCreateFormView.as_view(), name="nippo-create"),
    path("update/<int:pk>", nippoUpdateView, name="nippo-update"),
    path("delete/<int:pk>", nippoDeleteView, name="nippo-delete"),
]