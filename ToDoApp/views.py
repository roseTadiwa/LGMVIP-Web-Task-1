from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    if request.method == 'POST':
        new_item = TodoItem(text=request.POST['task'])
        new_item.save()
        return redirect('index')

    todo_items = TodoItem.objects.all()
    return render(request, 'index.html', {'todo_items': todo_items})

def complete(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('index')

def delete(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')