from .models import CaseModel
from django.contrib.sitemaps import Sitemap


class CaseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return CaseModel.objects.all()
    
    def lastmod(self, obj):
        obj.date