from django.urls import path
from .views import SarablogListView,SarablogDetailView,SarablogCreateView,SarablogUpdateView,SarablogDeleteView


urlpatterns = [
    path("post/new/", SarablogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", SarablogDetailView.as_view(), name="post_detail"),
    path("", SarablogListView.as_view(), name="home"),
    path("post/<int:pk>/edit/", SarablogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", SarablogDeleteView.as_view(), name="post_delete")
    ]