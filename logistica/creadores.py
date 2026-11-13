"""Creadores del patrón Factory Method: la clase base Logistica y sus subclases."""

from abc import ABC, abstractmethod

from logistica.transporte import Avion, Barco, Camion, Transporte


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


class LogisticaTerrestre(Logistica):
    """Creador concreto: produce camiones."""

    def crear_transporte(self) -> Transporte:
        return Camion()


class LogisticaMaritima(Logistica):
    """Creador concreto: produce barcos y reutiliza el ya creado (caché)."""

    def __init__(self) -> None:
        self._barco: Transporte | None = None

    def crear_transporte(self) -> Transporte:
        if self._barco is None:
            self._barco = Barco()
        return self._barco


class LogisticaAerea(Logistica):
    """Creador concreto: produce aviones."""

    def crear_transporte(self) -> Transporte:
        return Avion()
