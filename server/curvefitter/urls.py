from django.urls import path

from . import views

urlpatterns = [
    path("api/fit-curve/", views.fit_curve, name="fit_curve"),
]