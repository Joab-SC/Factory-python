"""Productos concretos: cada transporte implementa entrega() a su manera."""

from logistica.transporte import Transporte


class Camion(Transporte):
    """Producto concreto: entrega por tierra."""

    def entrega(self, destino: str) -> str:
        mensaje = f"Camión: entregando por tierra a {destino}"
        print(mensaje)
        return mensaje


class Barco(Transporte):
    """Producto concreto: entrega por mar."""

    def entrega(self, destino: str) -> str:
        mensaje = f"Barco: entregando por mar a {destino}"
        print(mensaje)
        return mensaje


class Avion(Transporte):
    """Producto concreto: entrega por aire."""

    def entrega(self, destino: str) -> str:
        mensaje = f"Avión: entregando por aire a {destino}"
        print(mensaje)
        return mensaje
