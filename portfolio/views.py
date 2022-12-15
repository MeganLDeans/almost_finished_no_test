from django.shortcuts import redirect, render
from .forms import UserImage
from .models import Portfolio
from django.views.generic import ListView, DetailView


def image_request(request):
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance

            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})
    else:
        form = UserImage()

    return render(request, 'image_form.html', {'form': form})


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "home.html"


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_detail.html"
