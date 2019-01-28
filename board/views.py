from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect
from django.views.generic.edit import ModelFormMixin
from django.utils import timezone
from django.http import JsonResponse
from django.views import generic
from .models import Board,Chat
from .forms import ChatCreateForm,BoardCreateForm

# Create your views here.
class IndexView(generic.ListView):
    model = Board
    paginate_by = 3

    def get_queryset(self):
        queryset = Board.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')

        if keyword:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(text__icontains = keyword)
            )

        return queryset

class CreateView(generic.CreateView):
    model = Board
    form_class= BoardCreateForm

    def form_valid(self,form):
        board = form
        board.save()
        return redirect('board:index')


class DetailView(ModelFormMixin,generic.DetailView):

    model = Board
    form_class =ChatCreateForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        return context


    def form_valid(self,form):

        board_pk = self.kwargs['pk']
        chat = form.save(commit=False)
        chat.board = get_object_or_404(Board,pk=board_pk)
        chat.save()
        return redirect('board:detail',pk=board_pk)



    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)


class JunleView(generic.ListView):
    mdoel = Board
    def get_queryset(self):
        junle_pk = self.kwargs['pk']
        queryset = Board.objects.order_by('-created_at').filter(junle_id = junle_pk)
        return queryset




def ajax_chat_add(request):

    name = request.POST.get('name')
    text = request.POST.get('text')
    board_pk = int(request.POST.get('board_pk'))
    board = list(Board.objects.filter(pk=board_pk))

    chat = Chat.objects.create(name = name,text=text,board=board[0])

    d = {
        'name': chat.name,
        'text': chat.text,
        'created_at': timezone.datetime.now().strftime("%Y年%-m月%-d日 %-H:%-M")
    }
    return JsonResponse(d)
