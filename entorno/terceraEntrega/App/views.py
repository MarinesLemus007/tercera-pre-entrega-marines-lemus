from django.shortcuts import render
from .forms import ClientForm, ProductoForm, SellerForm
from .models import Clients, Products, Sellers

# Create your views here.

def home(request):
    return render(request, "./app/base.html")

def client(request):
    if request.method =='POST':
        form = ClientForm(request.POST)

        if form.is_valid:
            form.save()
            return render(request, './app/home.html')
    else:
        form = ClientForm()
    return render(request, "./app/cliente.html", {"form": form})

def product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, './app/home.html')
    else:
        form = ProductoForm()
    return render(request, './app/producto.html', {'form': form})

def seller(request):
    if request.method =='POST':
        form = SellerForm(request.POST)

        if form.is_valid:
            form.save()
            return render(request, './app/home.html')
    else:
        form = SellerForm()
    return render(request, "./app/vendedor.html", {"form": form})

def buscar(request):

    q = request.GET.get('q', '')
    productos = Products.objects.filter(name__icontains=q)
 
    if productos:
        return render(request, './app/busqueda.html', {'productos': productos})
    else:
        mensaje = 'Producto no encontrado'
        return render(request, './app/busqueda.html', {'mensaje': mensaje})