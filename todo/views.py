from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    todos = Todo.objects.all().order_by("added_date")
    return render(request, 'index.html', {"todos": todos})


def add_todo(request):
    added_date = timezone.now()
    text = request.POST["content"]
    Todo.objects.create(added_date=added_date, text=text)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
