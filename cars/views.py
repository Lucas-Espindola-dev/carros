from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        # Nesse query, todos os modelos são retornados da mesma forma que retorna no objects.all().
        # O super faz referência a ListView. A utilização de super() é para invocar a herança.
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search).order_by('model')
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name="dispatch")
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    # Pagina seguinte.


@method_decorator(login_required(login_url='login'), name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
