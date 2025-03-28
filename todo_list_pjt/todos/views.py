from django.shortcuts import render,redirect
from . models import Todo
# Create your views here.


def index(request):
    works=Todo.objects.all()
    context = {
        'todo_list': works
    }
    return render(request, 'todos/index.html', context)


def create_todo(request):
    return render(request, 'todos/create_todo.html')


def detail(request, todo_pk):
    todo=Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def new(request):
 work = request.POST.get('work')
 content = request.POST.get('content')
 is_completed = False
 todo = Todo(work=work, content=content, is_completed=is_completed)
 todo.save()
 return redirect('todos:detail', todo.pk)

def delete(request,todo_pk):
   todo=Todo.objects.get(pk=todo_pk)
   todo.delete()
   return redirect("todos:index")

def update(request,todo_pk):
   todo=Todo.objects.get(pk=todo_pk)

   context={
      'context':todo
   }
   return render(request,'todos/update.html',context)

def update_input(request,todo_pk):
   work=request.POST.get('work')
   content=request.POST.get('content')
   todo=Todo.objects.get(pk=todo_pk)
   todo.work=work
   todo.content=content
   todo.save()
   return redirect('todos:detail', todo.pk)