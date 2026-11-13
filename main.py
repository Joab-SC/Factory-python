"""Cliente: elige el creador según la configuración y usa solo la interfaz Logistica."""

import argparse

from logistica.creadores import (
    Logistica,
    LogisticaAerea,
    LogisticaMaritima,
    LogisticaTerrestre,
)

CREADORES: dict[str, type[Logistica]] = {
    "terrestre": LogisticaTerrestre,
    "maritima": LogisticaMaritima,
    "aerea": LogisticaAerea,
}


def crear_logistica(modo: str) -> Logistica:
    """Devuelve el creador configurado para el modo indicado."""
    if modo not in CREADORES:
        raise ValueError(f"Modo desconocido: {modo}. Opciones: {', '.join(CREADORES)}")
    return CREADORES[modo]()


def cliente(logistica: Logistica, destino: str) -> None:
    """Trabaja con cualquier logística sin conocer su clase concreta."""
    logistica.planificar_entrega(destino)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gestión logística con Factory Method")
    parser.add_argument("--modo", choices=CREADORES.keys(), default="terrestre")
    parser.add_argument("--destino", default="Bogotá")
    args = parser.parse_args()

    cliente(crear_logistica(args.modo), args.destino)


if __name__ == "__main__":
    main()
