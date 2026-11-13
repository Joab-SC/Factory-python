"""Versión alternativa SIN Factory Method: el cliente decide la clase con if/elif."""

import argparse


class Camion:
    def entrega(self, destino: str) -> str:
        mensaje = f"Camión: entregando por tierra a {destino}"
        print(mensaje)
        return mensaje


class Barco:
    def entrega(self, destino: str) -> str:
        mensaje = f"Barco: entregando por mar a {destino}"
        print(mensaje)
        return mensaje


def planificar_entrega(modo: str, destino: str) -> str:
    """El cliente conoce y crea directamente cada clase concreta."""
    if modo == "terrestre":
        transporte: Camion | Barco = Camion()
    elif modo == "maritima":
        transporte = Barco()
    else:
        raise ValueError(f"Modo desconocido: {modo}")

    print(f"Planificando ruta hacia {destino}...")
    return transporte.entrega(destino)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gestión logística con if/elif")
    parser.add_argument("--modo", choices=["terrestre", "maritima"], default="terrestre")
    parser.add_argument("--destino", default="Bogotá")
    args = parser.parse_args()

    planificar_entrega(args.modo, args.destino)


if __name__ == "__main__":
    main()
