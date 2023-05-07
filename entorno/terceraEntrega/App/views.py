from django.shortcuts import render
from .forms import ClientForm, ProductoForm, SellerForm
from .models import Clients, Products, Sellers
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "./app/base.html")

def client(request):

    request.method == 'GET'
    clientes = Clients.objects.all()

    if request.method =='POST':
        form = ClientForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'El cliente se ha creado con éxito.')
            form = ClientForm()
            return render(request, "./app/cliente.html", {"form": form, "clientes": clientes})
    else:
        form = ClientForm()
    return render(request, "./app/cliente.html", {"form": form, "clientes": clientes})

def cliente_editar(request, cliente_id):
    cliente = get_object_or_404(Clients, pk=cliente_id)

    q = request.GET.get('q', '')
    productos = Products.objects.filter(name__icontains=q)

    if request.method == 'POST':
        nombre = request.POST.get('name')
        email = request.POST.get('email')

        cliente.name = nombre
        cliente.email = email

        cliente.save()

        return redirect('./app/cliente.html')

    return render(request, './app/cliente.html')

def cliente_eliminar(request, id_cliente):

    if(request.method == 'GET'):
        client = Clients.objects.get(id=id_cliente)
        client.delete()
        messages.success(request,'el Cliente se ha eliminado exitosamente.')
        return render(request, './app/cliente_eliminar.html')
    else:
        messages.success(request,'Hubo un erro al intentar borrar el usuario.')
        return render(request, './app/cliente_eliminar.html')

def product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se ha creado con éxito.')
            form = ProductoForm()
            return render(request, './app/producto.html', {'form': form})
    else:
        form = ProductoForm()
    return render(request, './app/producto.html', {'form': form})

def seller(request):
    if request.method =='POST':
        form = SellerForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'El vendedor se ha creado con éxito.')
            form = SellerForm()
            return render(request, "./app/vendedor.html", {"form": form})
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