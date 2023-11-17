from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from todo.models import Todo
from todo.forms import TodoForm
# Create your views here.


@login_required
def index(request):
    context = {"todos": Todo.objects.filter(user=request.user), "form": TodoForm()}
    return render(request, "index.html", context)



@login_required
@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
    return index(request)