from producto import Producto


class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def __str__(self):
        tienda_info = f"Tienda: {self.__nombre}, Costo de Delivery: {self.__costo_delivery}\nProductos:\n"
        for producto in self.__productos:
            tienda_info += str(producto) + "\n"
        return tienda_info

    # Getter para productos
    def get_productos(self):
        return self.__productos

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p == producto:
                p.aumentar_stock(producto.stock)
                break
        else:
            self.__productos.append(producto)

    def listar_productos(self):
        # Esta implementación es solo un placeholder.
        # Cada subclase de Tienda deberá proporcionar su propia implementación.
        raise NotImplementedError

    def realizar_venta(self, nombre_producto, cantidad):
        # Esta implementación es solo un placeholder.
        # Cada subclase de Tienda deberá proporcionar su propia implementación.
        raise NotImplementedError


class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        super().ingresar_producto(Producto(producto.nombre, producto.precio, 0))

    def listar_productos(self):
        # Utiliza el getter para acceder a la lista de productos
        return "\n".join([f"{p.nombre} - ${p.precio}" for p in self.get_productos()])

    def realizar_venta(self, nombre_producto, cantidad):
        # Implementación específica para Restaurante
        pass  # Los restaurantes no necesitan verificar el stock para vender


class Supermercado(Tienda):
    def listar_productos(self):
        productos_str = []
        for p in self.get_productos():
            stock_msg = "Pocos productos disponibles" if p.stock < 10 else ""
            productos_str.append(
                f"{p.nombre} - ${p.precio} - Stock: {p.stock} {stock_msg}"
            )
        return "\n".join(productos_str)

    def realizar_venta(self, nombre_producto, cantidad):
        # Implementación específica para Supermercado
        for p in self.get_productos():
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p.disminuir_stock(cantidad)
                else:
                    print(
                        f"Solo hay {p.stock} unidades disponibles de {nombre_producto}."
                    )
                    p.stock = 0
                break
        else:
            print(f"Producto {nombre_producto} no encontrado.")


class Farmacia(Tienda):
    def listar_productos(self):
        productos_str = []
        for p in self.get_productos():
            envio_msg = (
                "Envío gratis al solicitar este producto" if p.precio > 15000 else ""
            )
            productos_str.append(f"{p.nombre} - ${p.precio} {envio_msg}")
        return "\n".join(productos_str)

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print(
                "No se puede solicitar una cantidad superior a 3 por producto en cada venta."
            )
            return
        for p in self.get_productos():
            if p.nombre == nombre_producto:
                if p.stock >= cantidad:
                    p.disminuir_stock(cantidad)
                else:
                    print(f"No hay stock suficiente de {nombre_producto}.")
                break
        else:
            print(f"Producto {nombre_producto} no encontrado.")
