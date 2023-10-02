from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, DetailView, ListView
from .models import CaseModel, LocationCategory, PriceCategory
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cases'] = CaseModel.objects.order_by('-date')[:7]
        return context
    

class FileDetailView(DetailView):
    model = CaseModel
    template_name = 'pages/file.html'
    context_object_name = 'case'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'    


class FilesListView(ListView):
    model = CaseModel
    template_name = 'pages/files.html'
    context_object_name = 'cases'
    paginate_by = 12


class SearchListView(ListView): # A new page for search form.
    model = CaseModel
    template_name = 'pages/search.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        object_list = CaseModel.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        return object_list


class CategoryTemplateView(TemplateView):
    template_name = 'pages/categories.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['price_category'] = PriceCategory.objects.all()
        context['location_category'] = LocationCategory.objects.all()
        return context
    

class PriceRangeListView(ListView):
    model = CaseModel
    template_name = 'pages/price_range.html'
    paginate_by = 20

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cases'] = CaseModel.objects.all().filter(price_range_id__exact=self.kwargs['pk'])
        return context
    

class LocationsListView(ListView):
    model = CaseModel
    template_name = 'pages/locations.html'
    paginate_by = 20

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cases'] = CaseModel.objects.all().filter(location_id__exact=self.kwargs['pk'])
        return context