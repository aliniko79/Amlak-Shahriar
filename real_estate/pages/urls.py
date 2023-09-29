from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('<int:pk>/', FileDetailView.as_view(), name='file_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('files/', FilesListView.as_view(), name='files_page'),
]
