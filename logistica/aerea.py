"""Extensión: transporte aéreo agregado sin modificar las clases existentes."""

from logistica.creadores import Logistica
from logistica.transporte import Transporte


class Avion(Transporte):
    """Producto concreto: entrega por aire."""

    def entrega(self, destino: str) -> str:
        mensaje = f"Avión: entregando por aire a {destino}"
        print(mensaje)
        return mensaje


class LogisticaAerea(Logistica):
    """Creador concreto: produce aviones."""

    def crear_transporte(self) -> Transporte:
        return Avion()
