from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, DetailView, ListView
from .models import CaseModel
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


class SearchListView(ListView):
    model = CaseModel
    template_name = 'pages/search.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        object_list = CaseModel.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        return object_list
