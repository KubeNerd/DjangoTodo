from django.shortcuts import render,redirect
from .models import TaskBd
from .forms import ConteudoForm

# Create your views here.

def index(request):
    conteudo = TaskBd.objects.all()
    form = ConteudoForm()
    if request.method=='POST':
        form=ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/task')
    contexto = {
        'conteudo':conteudo,
        'form':form
    }
    return render(request,'lista.html', contexto)

def delete_task(request,id):
    deleteTask = TaskBd.objects.get(id=id)
    deleteTask.delete()
    return redirect('/task')