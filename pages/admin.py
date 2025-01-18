from django.contrib import admin
from .models import *


admin.site.register(CaseModel)
admin.site.register(LocationCategory)
admin.site.register(PriceCategory)
admin.site.register(TypeCategory)