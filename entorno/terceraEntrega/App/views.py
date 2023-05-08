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

def cliente_editar(request, id_cliente):
    client = Clients.objects.get(id=id_cliente)
    
    if(request.method == 'GET'):
        form = ClientForm(instance=client)
        return render(request, './app/cliente_editar.html', {"form": form, 'client': client})
        

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid:
            form.save()
            messages.success(request,'el Cliente se ha editado exitosamente.')
            return render(request, "./app/cliente_editar.html")
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Cliente.')
            return render(request, "./app/cliente.html")

def cliente_eliminar(request, id_cliente):

    if(request.method == 'GET'):
        client = Clients.objects.get(id=id_cliente)
        client.delete()
        messages.success(request,'el Cliente se ha eliminado exitosamente.')
        return render(request, './app/cliente_eliminar.html')
    else:
        messages.success(request,'Hubo un erro al intentar borrar el Cliente.')
        return render(request, './app/cliente_eliminar.html')

def product(request):

    request.method == 'GET'
    productos = Products.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se ha creado con éxito.')
            form = ProductoForm()
            return render(request, './app/producto.html', {'form': form, 'productos': productos})
    else:
        form = ProductoForm()
    return render(request, './app/producto.html', {'form': form, 'productos': productos})

def producto_editar(request, id_producto):
    producto = Products.objects.get(id=id_producto)
    
    if(request.method == 'GET'):
        form = ProductoForm(instance=producto)
        return render(request, './app/producto_editar.html', {"form": form, 'producto': producto})
        

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid:
            form.save()
            messages.success(request,'el Producto se ha editado exitosamente.')
            return render(request, "./app/producto_editar.html")
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Producto.')
            return render(request, "./app/producto.html")

def producto_eliminar(request, id_producto):

    if(request.method == 'GET'):
        producto = Products.objects.get(id=id_producto)
        producto.delete()
        messages.success(request,'el Producto se ha eliminado exitosamente.')
        return render(request, './app/producto_eliminar.html')
    else:
        messages.success(request,'Hubo un erro al intentar borrar el Producto.')
        return render(request, './app/producto_eliminar.html')


def seller(request):

    request.method == 'GET'
    vendedores = Sellers.objects.all()

    if request.method =='POST':
        form = SellerForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'El vendedor se ha creado con éxito.')
            form = SellerForm()
            return render(request, "./app/vendedor.html", {"form": form, "vendedores": vendedores})
    else:
        form = SellerForm()
    return render(request, "./app/vendedor.html", {"form": form, "vendedores": vendedores})

def vendedor_editar(request, id_vendedor):
    vendedor = Sellers.objects.get(id=id_vendedor)
    
    if(request.method == 'GET'):
        form = SellerForm(instance=vendedor)
        return render(request, './app/vendedor_editar.html', {"form": form, 'vendedor': vendedor})
        

    if request.method == 'POST':
        form = SellerForm(request.POST, instance=vendedor)

        if form.is_valid:
            form.save()
            messages.success(request,'el Vendedor se ha editado exitosamente.')
            return render(request, "./app/vendedor_editar.html")
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Vendedor.')
            return render(request, "./app/vendedor.html")

def vendedor_eliminar(request, id_vendedor):

    if(request.method == 'GET'):
        vendedor = Sellers.objects.get(id=id_vendedor)
        vendedor.delete()
        messages.success(request,'el Vendedor se ha eliminado exitosamente.')
        return render(request, './app/vendedor_eliminar.html')
    else:
        messages.success(request,'Hubo un erro al intentar borrar al Vendedor.')
        return render(request, './app/vendedor_eliminar.html')

def buscar(request):

    q = request.GET.get('q', '')
    productos = Products.objects.filter(name__icontains=q)
 
    if productos:
        return render(request, './app/busqueda.html', {'productos': productos})
    else:
        mensaje = 'Producto no encontrado'
        return render(request, './app/busqueda.html', {'mensaje': mensaje})