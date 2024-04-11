class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = max(value, 0)

    def __eq__(self, otro):
        return self.__nombre == otro.__nombre

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"

    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad  # Usa el setter para stock

    def disminuir_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad  # Usa el setter para stock
