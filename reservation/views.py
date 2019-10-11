from django.shortcuts import render, redirect

# Create your views here.
from .models import Reservation
from .forms import ReservationForm, ReservationPasswordForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class Reservation_List(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'
    paginate_by = 3


class Reservation_Create(CreateView):
    model = Reservation
    fields = '__all__'
    template_name = 'reservation/reservation_create.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = ReservationForm()
        if request.POST:
            return render(request, self.template_name)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation:list')
        return self.render_to_response({'form':form})

class Reservation_Update(UpdateView):
    model = Reservation
    fields = '__all__'
    template_name = 'reservation/reservation_update.html'
    success_url = reverse_lazy('reservation:list')


class Reservation_Delete(DeleteView):
    model = Reservation
    template_name = 'reservation/reservation_delete.html'
    success_url = '/'


class Reservation_Detail(FormMixin, DetailView):
    model = Reservation
    template_name = 'reservation/reservation_detail.html'

    def get(self, request, *args, **kwargs):
        form = ReservationPasswordForm()
        if request.POST:
            return render(request, self.template_name)
        object = self.get_object()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args,**kwargs):
        object = self.get_object()
        form = ReservationPasswordForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == object.password:
                # form = AppointmentPasswordForm(request.POST)
                return render(request, self.template_name,{'object': object})

        return render(request, self.template_name, {'form': form})
