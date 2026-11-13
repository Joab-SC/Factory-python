"""Productos del patrón Factory Method: la interfaz Transporte y sus implementaciones."""

from abc import ABC, abstractmethod


class Transporte(ABC):
    """Producto: interfaz común que deben cumplir todos los transportes."""

    @abstractmethod
    def entrega(self, destino: str) -> str:
        """Realiza la entrega en el destino y devuelve una descripción de ella."""


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
