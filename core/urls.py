from django.urls import path
from core.views import StudentListDataTable, StudentListView

urlpatterns = [
    path("student-list/", StudentListView.as_view(), name="student-list"),
    path("student-list-json/", StudentListDataTable.as_view(), name="student-list-json"),
]