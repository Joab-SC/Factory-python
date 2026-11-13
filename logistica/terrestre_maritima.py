"""Creadores concretos para transporte terrestre y marítimo."""

from logistica.creadores import Logistica
from logistica.transporte import Barco, Camion, Transporte


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
