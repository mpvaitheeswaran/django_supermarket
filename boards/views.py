from django.shortcuts import render,redirect
from boards.models import Board
from django.views.generic import ListView

from products.models import Product

# Create your views here.
# def boards(request):
#     context = Board.objects.all()
#     return render(request,'boards/kanban_board.html')

class BoardList(ListView):
    model = Board
    template_name = 'boards/kanban_board.html'
    context_object_name = 'items'

def moveProduct(request):
    if request.method == 'POST':
        productId = int(request.POST.get('product_id'))
        columnId = int(request.POST.get('column_id'))
        product = Product.objects.get(pk=productId)
        product.column = columnId
        product.save()
        return redirect('boards')