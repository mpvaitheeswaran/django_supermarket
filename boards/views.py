from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from boards.models import Board
from django.views.generic import ListView
import json
from products.models import Product

# Create your views here.
# def boards(request):
#     context = Board.objects.all()
#     return render(request,'boards/kanban_board.html')

class BoardList(ListView):
    model = Board
    template_name = 'boards/kanban_board.html'
    context_object_name = 'items'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['products'] = Product.objects.filter(user=self.request.user)
        boards = super().get_context_data(**kwargs)['items']
        products = list(Product.objects.filter(user=self.request.user))
        
        for board in boards:
            for product in products:
                if board.product.id == product.id:
                    #remove the curent product in products
                    products.remove(product)
        context['products'] = products    
        return context

def moveProduct(request):
    if request.method == 'POST':
        productId = int(request.POST.get('product_id'))
        columnId = int(request.POST.get('column_id'))
        product = Product.objects.get(pk=productId)
        product.column = columnId
        product.save()
        return redirect('boards')

def addProductBoard(request):
    if request.method == 'GET' and request.is_ajax():
        productIds = request.GET.getlist('selectedProIds[]')
        ids =[] 
        names = []
        for id in productIds:
            product = Product.objects.get(pk=id)
            Board.objects.create(product=product)
            ids.append(product.id) 
            names.append(product.name) 
        return HttpResponse(json.dumps({'id': ids, 'name': names}), content_type="application/json")