from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, DetailView, ListView
from .models import *
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['price_category'] = PriceCategory.objects.all()
        context['location_category'] = LocationCategory.objects.all()
        context['type_categoty'] = TypeCategory.objects.all()
        return context


class FilteredFilesListView(ListView):
    model = CaseModel
    template_name = 'pages/filtered.html'
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Any]:
        q1 = self.request.GET.get('q1')
        q2 = self.request.GET.get('q2')
        q3 = self.request.GET.get('q3')
        if q1!='NULL' and q2!='NULL' and q3!='NULL':
            object_list = CaseModel.objects.filter(
                Q(price_range_id__exact=q1) & Q(location_id__exact=q2) & Q(type_r_id__exact=q3)
            )
            return object_list
        elif q1!='NULL' and q2!='NULL':
            object_list = CaseModel.objects.filter(
                Q(price_range_id__exact=q1) & Q(location_id__exact=q2)
            )
            return object_list
        elif q1!='NULL' and q3!='NULL':
            object_list = CaseModel.objects.filter(
                Q(price_range_id__exact=q1) & Q(type_r_id__exact=q3)
            )
            return object_list
        elif q2!='NULL' and q3!='NULL':
            object_list = CaseModel.objects.filter(
                Q(location_id__exact=q2) & Q(type_r_id__exact=q3)
            )
            return object_list
        elif q1!='NULL':
            object_list = CaseModel.objects.filter(
                Q(price_range_id__exact=q1)
            )
            return object_list
        elif q2!='NULL' :
            object_list = CaseModel.objects.filter(
                Q(location_id__exact=q2)
            )
            return object_list
        elif q3!='NULL':
            object_list = CaseModel.objects.filter(
                Q(type_r_id__exact=q3)
            )
            return object_list
        object_list = CaseModel.objects.all()
        return object_list
    

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
        context['type_category'] = TypeCategory.objects.all()
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
    

class TypesListView(ListView):
    model = CaseModel
    template_name = 'pages/types.html'
    paginate_by = 20

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cases'] = CaseModel.objects.all().filter(type_r_id__exact=self.kwargs['pk'])
        return context