#!/usr/bin/env python 
__author__ = "Megan Deans"
from django.urls import path
from .views import image_request
from .views import PortfolioListView, PortfolioDetailView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView
urlpatterns = [
    path("portfolio/<int:pk>/", PortfolioDetailView.as_view(), name="portfolio_detail"),
    path("", PortfolioListView.as_view(), name="home"),
    path("porfolio/home", PortfolioListView.as_view(), name ="portfolio_home"),
    path("", image_request, name="image"),
    path("portfolio/new/", PortfolioCreateView.as_view(), name="portfolio_new"),
    path("portfolio/<int:pk>/edit/", PortfolioUpdateView.as_view(), name="portfolio_edit"),
    path("portfolio/<int:pk>/delete/", PortfolioDeleteView.as_view(), name="portfolio_delete"),
]