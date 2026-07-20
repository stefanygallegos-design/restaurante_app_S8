from modelos.producto import Producto


class Bebida(Producto):
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        envase: str,
    ):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = tamano
        self.envase = envase

    def mostrar_informacion(self) -> str:
        return (
            super().mostrar_informacion()
            + f"\nTamaño: {self.tamano}"
            + f"\nEnvase: {self.envase}"
        )
