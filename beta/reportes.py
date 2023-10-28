# Función para generar reporte de ventas por cliente
def generar_reporte_ventas_por_cliente():
    # Diccionario para almacenar las ventas por cliente
    ventas_por_cliente = {}

    for venta in ventas:
        codigo_cliente = venta.codigo_cliente
        total_venta = venta.total_venta

        if codigo_cliente in ventas_por_cliente:
            ventas_por_cliente[codigo_cliente] += total_venta
        else:
            ventas_por_cliente[codigo_cliente] = total_venta

    print("Reporte de Ventas por Cliente:")
    for codigo_cliente, total_venta in ventas_por_cliente.items():
        print(f"Código de Cliente: {codigo_cliente}, Total de Ventas: {total_venta}")

def generar_reporte_ventas_por_producto():
    # Diccionario para almacenar las ventas por producto
    ventas_por_producto = {}

    for venta in ventas:
        codigo_producto = venta.codigo_producto
        cantidad_venta = venta.cantidad

        if codigo_producto in ventas_por_producto:
            ventas_por_producto[codigo_producto] += cantidad_venta
        else:
            ventas_por_producto[codigo_producto] = cantidad_venta

    print("Reporte de Ventas por Producto:")
    for codigo_producto, cantidad_venta in ventas_por_producto.items():
        print(f"Código de Producto: {codigo_producto}, Cantidad Vendida: {cantidad_venta}")

# Menú de opciones
while True:
    print("---- Menú de Operaciones ----")
    print("1. Generar reporte de ventas por cliente")
    print("2. Generar reporte de ventas por producto")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        generar_reporte_ventas_por_cliente()
    elif opcion == '2':
        generar_reporte_ventas_por_producto()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
