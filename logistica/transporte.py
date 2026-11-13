"""Producto del patrón Factory Method: la interfaz Transporte."""

from abc import ABC, abstractmethod


class Transporte(ABC):
    """Producto: interfaz común que deben cumplir todos los transportes."""

    @abstractmethod
    def entrega(self, destino: str) -> str:
        """Realiza la entrega en el destino y devuelve una descripción de ella."""
