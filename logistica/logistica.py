"""Creadora del patrón Factory Method: la clase abstracta Logistica."""

from abc import ABC, abstractmethod

from logistica.transporte import Transporte


class Logistica(ABC):
    """Creadora: declara el método fábrica y contiene la lógica de negocio.

    No conoce ninguna clase concreta de transporte; solo trabaja con la
    interfaz Transporte.
    """

    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """Método fábrica: las subclases deciden qué transporte devolver."""

    def planificar_entrega(self, destino: str) -> str:
        """Planifica la ruta y realiza la entrega con el transporte creado."""
        transporte = self.crear_transporte()
        print(f"Planificando ruta hacia {destino}...")
        return transporte.entrega(destino)
