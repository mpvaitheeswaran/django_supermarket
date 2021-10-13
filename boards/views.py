from django.shortcuts import render
from boards.models import Board
from django.views.generic import ListView

# Create your views here.
# def boards(request):
#     context = Board.objects.all()
#     return render(request,'boards/kanban_board.html')

class BoardList(ListView):
    model = Board
    template_name = 'boards/kanban_board.html'
    context_object_name = 'items'