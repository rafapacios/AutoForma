from django.contrib import admin
from  catalogo.models import prodCad
from import_export.admin import ImportExportModelAdmin

class produtos(admin.ModelAdmin):
    model = prodCad
    list_display = ('id','marca','cod_fab','cod_int','cat','modelo','desc','preco','cor')
    list_filter = ('marcabusca', 'desc')

class produtos(ImportExportModelAdmin):
    model = prodCad
    list_display = ('id','marca', 'cod_fab', 'cod_int', 'cat', 'modelo', 'desc', 'preco', 'cor')
    list_filter = ('marcabusca', 'cat')


admin.site.register(prodCad, produtos)

