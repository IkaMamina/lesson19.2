from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product


class CatalogListView(ListView):
    model = Product


class CatalogDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter +=1
        self.object.save()
        return self.object


class CatalogCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:catalog_list")


class CatalogUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy("catalog:catalog_list")

    def get_success_url(self):
        return reverse('catalog:catalog_detail', args=[self.kwargs.get('pk')])


class CatalogDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:catalog_list")
