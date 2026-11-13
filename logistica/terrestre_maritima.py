"""Creadores concretos para transporte terrestre y marítimo."""

from logistica.creadores import Logistica
from logistica.transporte import Barco, Camion, Transporte


class LogisticaTerrestre(Logistica):
    """Creador concreto: produce camiones."""

    def crear_transporte(self) -> Transporte:
        return Camion()


class LogisticaMaritima(Logistica):
    """Creador concreto: produce barcos."""

    def crear_transporte(self) -> Transporte:
        return Barco()
