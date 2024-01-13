from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from core.models import Student
from django.shortcuts import render
from django.views import View


class StudentListDataTable(BaseDatatableView):
    model = Student
    columns = ['name', 'age', 'city', 'email']
    order_columns = ['name', 'age', 'email', 'city']
    max_display_length = 100

    def render_column(self, row, column):
        if column == 'email':
            return f"<a href='mailto:{row.email}'>{row.email}</a>"
        elif column == 'name':
            return "<a href='https://www.google.com/search?q={0}' target='_blank'>{1}</a>".format(row.name, row.name)
        else:
            return super().render_column(row, column)
    
    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)
        return qs.filter(age__gt=20)
    
    def get_initial_queryset(self):
        # return queryset used as base for further sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. 
        # This is because we need some base queryset to count total number of records.

        # only filter those students whose email contains 'gmail'
        return Student.objects.filter(email__contains='gmail')
    
    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                self.render_column(item, 'name'),
                escape("{0}".format(item.age)),
                escape("{0}".format(item.city)),
                self.render_column(item, 'email'),
            ])
        return json_data
    


class StudentListView(View):
    def get(self, request):
        return render(request, "student_list.html")