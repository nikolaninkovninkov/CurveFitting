from django.urls import path

from . import views

urlpatterns = [
    path("fit-curve/", views.fit_curve, name="fit_curve"),
    path("newtons-method/", views.newtons_method, name="newtons_method"),

]