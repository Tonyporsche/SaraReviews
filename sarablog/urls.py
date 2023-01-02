from django.urls import path
from .views import SarablogListView,SarablogDetailView


urlpatterns = [
    path("post/<int:pk>/", SarablogDetailView.as_view(), name="post_detail"),
    path("", SarablogListView.as_view(), name="home"),
]