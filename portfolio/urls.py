#!/usr/bin/env python 
__author__ = "Megan Deans"
from django.urls import path
from .views import image_request
from .views import PortfolioListView
urlpatterns = [
    path("", PortfolioListView.as_view(), name="home"),
]

urlpatterns = [
    path("", image_request, name="image-request")
]