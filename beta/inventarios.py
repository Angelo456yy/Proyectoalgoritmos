import argparse

#donde se almacena lo de la lista
inventarios = []

#funciones para listar
def listar():
    if inventarios:
        print("Productos que existen en el inventario: ")
        for producto in inventarios:
            print(f"Codigo: {producto['codigo']}, Nombre: {producto['nombre']}, Existencia: {producto['existencia']}, Proveedor: {producto['proveedor']}, Precio: {producto['precio']}")
    else:
        print("No hay productos en el inventario.")
#funcion para crear productos

def crear(codigo, nombre, existencia, proveedor, precio):
    producto = {'codigo': codigo, 'nombre': nombre, 'existencia': existencia, 'proveedor': proveedor, 'precio': precio}
    inventarios.append(producto)
    # Guardar la información del producto en una variable global
    global nuevo_producto
    nuevo_producto = producto
    print("El producto ha sido añadido")

 #funcion para actualizar
def actualizar(codigo,precio_nuevo):
    for producto in inventarios:
        if producto['codigo']==codigo:  
            producto['precio']=precio_nuevo
            print(f"Precio del producto '{producto['nombre']}' actualizado a {precio_nuevo}.")
            return
        
    print(f"No se pudo encontrar ningún producto con el código '{codigo}'.")

        
#nueva funcion para existencia de productos
def editar_existencia(codigo, existencia_nueva):
    for producto in inventarios:
        if producto['codigo'] == codigo:
            producto['existencia'] = existencia_nueva
            print(f"La existencia del producto '{producto['nombre']}' fue actualizada a {existencia_nueva}.")
            return
    print(f"No se pudo encontrar ningún producto con el código '{codigo}'.")

#funcion con la cual eliminaremos los productos
def eliminar(codigo):
    for producto in inventarios:
        if producto['codigo'] == codigo:
            inventarios.remove(producto)
            print(f"Producto con código '{codigo}' se eliminado correctamente.")
            return
    print(f"No se pudo encontrar ningún producto con el código '{codigo}'.")


# Configuración de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Gestión de inventario de productos")
subparsers = parser.add_subparsers(dest='comando')

# Comando para listar productos
listar_parser = subparsers.add_parser('listar', help="Listar productos en el inventario")

# Comando para crear un producto
crear_parser = subparsers.add_parser('crear', help="Crear un nuevo producto")
crear_parser.add_argument('codigo', type=str, help="Código del producto")
crear_parser.add_argument('nombre', type=str, help="Nombre del producto")
crear_parser.add_argument('existencia', type=int, help="Existencia del producto")
crear_parser.add_argument('proveedor', type=str, help="Proveedor del producto")
crear_parser.add_argument('precio', type=float, help="Precio del producto")

# Comando para actualizar el precio de un producto
actualizar_parser = subparsers.add_parser('actualizar', help="Actualizar el precio de un producto")
actualizar_parser.add_argument('codigo', type=str, help="Código del producto")
actualizar_parser.add_argument('nuevo_precio', type=float, help="Nuevo precio del producto")

# Comando para editar la existencia de un producto
existencia_parser = subparsers.add_parser('existencia', help="Editar la existencia de un producto")
existencia_parser.add_argument('codigo', type=str, help="Código del producto")
existencia_parser.add_argument('nueva_existencia', type=int, help="Nueva existencia del producto")

# Comando para eliminar un producto
eliminar_parser = subparsers.add_parser('eliminar', help="Eliminar un producto")
eliminar_parser.add_argument('codigo', type=str, help="Código del producto")

# Función principal para ejecutar comandos
# Función principal para ejecutar comandos
def main():
    args = parser.parse_args()
    
    if args.comando == 'listar':
        listar()
    elif args.comando == 'crear':
        # Crear un producto
        crear(args.codigo, args.nombre, args.existencia, args.proveedor, args.precio)
    elif args.comando == 'actualizar':
        actualizar(args.codigo, args.nuevo_precio)
    elif args.comando == 'existencia':
        editar_existencia(args.codigo, args.nueva_existencia)
    elif args.comando == 'eliminar':
        eliminar(args.codigo)
    else:
        print("Comando no válido. Ejecuta 'python mi-proyecto.py --help' para ver las opciones disponibles.")

if __name__ == "__main__":
    main()






    
    
        