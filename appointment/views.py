from django.shortcuts import render, redirect

# Create your views here.
from .models import Appointment
from .forms import AppointmentForm, AppointmentPasswordForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class Appointment_List(ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'
    paginate_by = 3


class Appointment_Create(CreateView):
    model = Appointment
    fields = '__all__'
    template_name = 'appointment/appointment_create.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = AppointmentForm()
        if request.POST:
            return render(request, self.template_name)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment:list')
        return self.render_to_response({'form':form})

class Appointment_Update(UpdateView):
    model = Appointment
    fields = '__all__'
    template_name = 'appointment/appointment_update.html'
    success_url = reverse_lazy('appointment:list')


class Appointment_Delete(DeleteView):
    model = Appointment
    template_name = 'appointment/appointment_delete.html'
    success_url = '/'


class Appointment_Detail(FormMixin, DetailView):
    model = Appointment
    template_name = 'appointment/appointment_detail.html'

    def get(self, request, *args, **kwargs):
        form = AppointmentPasswordForm()
        if request.POST:
            return render(request, self.template_name)
        object = self.get_object()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args,**kwargs):
        object = self.get_object()
        form = AppointmentPasswordForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == object.password:
                #form = AppointmentPasswordForm(request.POST)
                return render(request, self.template_name,{'object': object})

        return render(request, self.template_name, {'form': form})
