from django.shortcuts import redirect, render
from .forms import UserImage
from .models import Portfolio
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def image_request(request):
    if request.method == 'POST':
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance

            return render(request, 'image.html', {'form': form, 'img_obj': img_object})
    else:
        form = UserImage()

    return render(request, 'image.html', {'form': form})


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio_home.html"


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio_detail.html"


class PortfolioCreateView(CreateView):
    model = Portfolio
    template_name = "portfolio_new.html"
    fields = '__all__'


class PortfolioUpdateView(UpdateView):
    model = Portfolio
    template_name = "portfolio_edit.html"
    fields = '__all__'


class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = "portfolio_delete.html"
    success_url = reverse_lazy("home")
