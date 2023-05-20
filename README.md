# Proyecto Final con Django

Consta de cuatro Modelos:

Clients, Products, Sellers y Avatar.

Cada una con sus formularios asociados:

ClientForm, ProductoForm, SellerForm y AvatarFormulario.

se puede realizar un CRUD (Create, Read, Updatey Delete) con los Clientes, Productos y Vendedores que se almacenan en la base de datos sqlite3 desde el front.

Tiene también una función para buscar productos según su nombre. Se puede registrar, realizar login, logout y subir avatar.

Se realizaron cuatro tests para evaluar:

- ✅ Creación de clientes
- ✅ Creación de productos
- ✅ Lectura de imagen por default de producto cuando no se proporciona
- ✅ Comprobación de sku único en producto creado.

Se ocupó la librería Pillow para trabajar con imágenes en los modelos. Para instalarla, se debe ejecutar el comando:

```
pip install pillow
```

Se deja url para visualizar el proyecto [GitHub Pages](https://pages.github.com/).

Se deja url de explicación del proyecto en youtube [youTube](https://pages.github.com/).