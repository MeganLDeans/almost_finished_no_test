#!/usr/bin/env python 
__author__ = "Megan Deans"
from django.urls import path
from .views import image_request
from .views import PortfolioListView, PortfolioDetailView
urlpatterns = [
    path("portfolio/<int:pk>/", PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("", PortfolioListView.as_view(), name="home"),
    path("", image_request, name="image-request")
]