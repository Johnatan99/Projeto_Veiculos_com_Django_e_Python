from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    #Mostrando todos dados:
    #data['db'] = Carros.objects.all()

    #Busca ---------------------------------
    data = {}
    search = request.GET.get('search') # Variável search recebe dados de um atributo do HTML através
                                       # do request, chamando o .GET que chama o atributo .get() com
                                       # o nome do atributo passado como parâmetro.
    
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search) # Acessando método .filter() para
                                                                     # realizar a busca de acordo com a busca.
    else:
        data['db'] = Carros.objects.all()

    return render(request, 'index.html', data)

    #Mostrando dados com paginação:
    #all = Carros.objects.all()
    #paginator = Paginator(data, 2)
    #pages = request.GET.get('page')
    #data['db'] = paginator.get_page(pages)
    #return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return  render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')