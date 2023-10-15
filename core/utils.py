from typing import Any
from django.contrib.admin import ModelAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest


class SandBoxCustomModelAdmin(ModelAdmin):
    using = "sandbox"

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.save(using=self.using)
    
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).using(self.using)
