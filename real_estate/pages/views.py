from typing import Any
from django.views.generic import TemplateView, DetailView, ListView
from .models import CaseModel


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
