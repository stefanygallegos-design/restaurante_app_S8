from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto):

        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Ya existe un producto con ese código.")
                return

        self.productos.append(producto)
        print("Producto registrado correctamente.")

    def registrar_cliente(self, cliente: Cliente):

        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print("Ya existe un cliente con esa identificación.")
                return

        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    def listar_productos(self):

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\nLISTA DE PRODUCTOS\n")

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 40)

    def listar_clientes(self):

        if not self.clientes:
            print("No existen clientes registrados.")
            return

        print("\nLISTA DE CLIENTES\n")

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
            print("-" * 40)
