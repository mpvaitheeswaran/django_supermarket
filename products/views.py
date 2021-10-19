from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalDeleteView,BSModalUpdateView,BSModalReadView
from .forms import ProductCreationForm
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

def myProductsData(request):
    data = dict()
    if request.method == 'GET':
        products = Product.objects.filter(user=request.user)
        # asyncSettings.dataKey = 'table'
        data['table'] = render_to_string(
            'products/_product_table.html',
            {'page_obj': products},
            request=request
        )
        return JsonResponse(data)
class ProductList(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 5
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            object_list = self.model.objects.filter(name__icontains=search)
        else:
            object_list = self.model.objects.all()
        return object_list

class MyProductList(LoginRequiredMixin,ListView):
    model = Product
    template_name = 'products/my_product_list.html'
    paginate_by = 5
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(user=self.request.user)
        return context
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            object_list = self.model.objects.filter(name__icontains=search)
        else:
            object_list = self.model.objects.filter(user=self.request.user)
        return object_list

# Bootstrap Modal form
class ProductCreateView(BSModalCreateView):
    template_name = 'products/product_create.html'
    form_class = ProductCreationForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('my_product_list')

class ProductReadView(BSModalReadView):
    model = Product
    template_name = 'products/product_read.html'
    
class ProductUpdateView(BSModalUpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductCreationForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('my_product_list')

class ProductDeleteView(BSModalDeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    
    success_message = 'Success: Product was deleted.'
    success_url = reverse_lazy('my_product_list')

# Async Delete
def deleteProduct(request):
    if request.method=='POST':
        product_ids = request.POST.getlist('ids[]')
        for id in product_ids:
            product = Product.objects.get(pk=id)
            product.delete()
        return redirect('my_products')
