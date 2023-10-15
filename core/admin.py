from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Author, Book, Person
from .forms import AuthorForm
from core.utils import SandBoxCustomModelAdmin
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    list_display = ('name', 'last_name')
    search_fields = ('name',)
    # list_display use to display the fields in the list view
    # fields are the fields that will be displayed in the detail view
    fields = form._meta.fields

    def get_search_results(self, request: HttpRequest, queryset: QuerySet[Any], search_term: str) -> tuple[QuerySet[Any], bool]:
        use_distinct  = True
        if not search_term:
            return queryset.filter(id__lte=10), use_distinct
        else:
            return super().get_search_results(request, queryset, search_term)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('log_user'):
            print(form.cleaned_data)
        super().save_model(request, obj, form, change)
    
@admin.register(Book)
class SandboxBookAdmin(SandBoxCustomModelAdmin):
    # add alternative name for the model to be appear in the admin
    # get the model name from the model meta class

    verbose_name = "Sandbox Book"