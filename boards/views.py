from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from boards.models import Board
from django.views.generic import ListView
import json
from products.models import Product
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalDeleteView,BSModalUpdateView,BSModalReadView
from products.forms import ProductCreationForm
from django.urls import reverse_lazy
from notifications.signals import notify
from notifications.models import Notification
from django.contrib.auth.models import User


def myProductsData(request):
    data = dict()
    if request.method == 'GET':
        boards = Board.objects.all()
        products_queryset = Product.objects.filter(user=request.user)
        boards = []
        #Filtering the borad objects for current user
        for product_query in products_queryset:
            if request.user == product_query.user:
                try:
                    boards.append(Board.objects.get(product=product_query))
                except:
                    print('Does not exist exception')
        # asyncSettings.dataKey = 'board'
        data['boardcard'] = render_to_string(
            'boards/_board.html',
            {'items': boards},
            request=request
        )
        return JsonResponse(data)

class BoardList(ListView):
    model = Board
    template_name = 'boards/kanban_board.html'
    context_object_name = 'items'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_queryset = Product.objects.filter(user=self.request.user)
        context['items'] = []
        #Filtering the borad objects for current user
        for product_query in products_queryset:
            if self.request.user == product_query.user:
                try:
                    context['items'].append(Board.objects.get(product=product_query))
                except:
                    print('Does not exist exception')
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
        if columnId == 3:
            verb = 'The task {0} is Done.'.format(product.name)
            notify.send(request.user, recipient=request.user, verb=verb)
        product.save()
        return redirect('boards')

def addProductBoard(request):
    if request.method == 'GET' and request.is_ajax():
        productIds = request.GET.getlist('selectedProIds[]')
        ids =[] 
        names = []
        boardIds =[]
        for id in productIds:
            product = Product.objects.get(pk=id)
            board = Board.objects.create(product=product)
            ids.append(product.id) 
            names.append(product.name) 
            boardIds.append(board.id)
        return HttpResponse(json.dumps({'id': ids, 'name': names,'boardid':boardIds}), content_type="application/json")

class ProductUpdateView(BSModalUpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductCreationForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('my_product_list')

def deleteBoard(request):
    if request.method == 'GET' and request.is_ajax():
        boardId = request.GET.get('id')
        board=Board.objects.get(pk=boardId)
        board.delete()
        print(boardId)
        return redirect('boards')

def readAllNotifications(request):
    user = User.objects.get(pk=request.user.id)
    unread = user.notifications.unread()
    unread.mark_all_as_read()
    return redirect('boards')

def readNotification(request,id):
    unread = Notification.objects.get(id=id)
    unread.mark_as_read()
    return redirect('boards')