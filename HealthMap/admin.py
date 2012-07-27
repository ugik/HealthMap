from django.contrib import admin
from HealthMap.models import *
        
class RangeAdmin(admin.ModelAdmin):
    list_display = ('low', 'high', 'color', 'name', 'dataset')
    search_fields = ['name']
    ordering = ('low',)

class DatarowAdmin(admin.ModelAdmin):
    list_display = ('dataset', 'region', 'value')
    search_fields = ['dataset']
    ordering = ('dataset', 'region',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('state', 'county')
    search_fields = ['state']
    ordering = ('state',)
    
admin.site.register(Region, RegionAdmin)
admin.site.register(Polyline)
admin.site.register(Category)
admin.site.register(Dataset)
admin.site.register(Range, RangeAdmin)
admin.site.register(Datarow, DatarowAdmin)
admin.site.register(History)

