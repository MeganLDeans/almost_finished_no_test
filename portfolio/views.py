from django.forms import forms
from django.views.generic import ListView, DetailView
from .models import Portfolio


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "home.html"


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_detail.html"



class imageForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "main_img"]