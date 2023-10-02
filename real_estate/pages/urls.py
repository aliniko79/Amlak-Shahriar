from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    re_path(r'files/(?P<slug>[-\w]+)/', FileDetailView.as_view(), name='file_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('files/', FilesListView.as_view(), name='files_page'),
    path('search/', SearchListView.as_view(), name='search_results'),
    path('categories/', CategoryTemplateView.as_view(), name='categories_page'),
    path('categories/price_range/<int:pk>/', PriceRangeListView.as_view(), name='price_page'),
    path('categories/location/<int:pk>/', LocationsListView.as_view(), name='location_page'),
]
