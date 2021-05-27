from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy

import csv

from .models import Record
from .forms import RecordForm, TemplateForm
from .utils import generate_csv_name, change_phone


@login_required(login_url='/login')
def home(request):
    records = Record.objects.filter(user__id=request.user.id)
    return render(request, 'templates_records/home.html', {'object_list': records})


@login_required(login_url='/login')
def template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            record_fields = request.POST.getlist('record_fields')
            name_fields = request.POST.getlist('name_fields')
            response = HttpResponse(
                content_type='text/csv',
                headers={f'Content-Disposition': f'attachment; filename="{generate_csv_name(name_fields, request)}"'},
            )
            records = Record.objects.filter(user__id=request.user.id).values_list('id', *tuple(record_fields))

            writer = csv.writer(response)
            writer.writerow(['id', *record_fields])
            for record in records:
                record = change_phone(record, record_fields)
                writer.writerow(record)
            return response
    else:
        form = TemplateForm()
    return render(request, 'templates_records/template.html', {'form': form})


class RecordDetailView(LoginRequiredMixin, DetailView):
    queryset = Record.objects.all()
    context_object_name = 'object'
    login_url = '/login'
    template_name = 'templates_records/detail.html'


class RecordCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = "templates_records/create.html"
    login_url = '/login'
    success_message = 'Record created succesfully!'
    success_url = reverse_lazy('templates_records:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
