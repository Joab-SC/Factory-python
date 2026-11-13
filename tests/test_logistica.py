"""Pruebas del patrón Factory Method aplicado a la gestión logística."""

import io
import unittest
from contextlib import redirect_stdout

from logistica.creadores import (
    Logistica,
    LogisticaAerea,
    LogisticaMaritima,
    LogisticaTerrestre,
)
from logistica.transporte import Avion, Barco, Camion, Transporte


class TestLogistica(unittest.TestCase):
    def setUp(self) -> None:
        self.creadores: list[Logistica] = [
            LogisticaTerrestre(),
            LogisticaMaritima(),
            LogisticaAerea(),
        ]

    def test_cada_creador_devuelve_el_producto_esperado(self) -> None:
        self.assertIsInstance(LogisticaTerrestre().crear_transporte(), Camion)
        self.assertIsInstance(LogisticaMaritima().crear_transporte(), Barco)
        self.assertIsInstance(LogisticaAerea().crear_transporte(), Avion)

    def test_todos_los_productos_cumplen_la_interfaz_transporte(self) -> None:
        for producto in (Camion, Barco, Avion):
            with self.subTest(producto=producto.__name__):
                self.assertTrue(issubclass(producto, Transporte))
                self.assertIsInstance(producto(), Transporte)

    def test_planificar_entrega_funciona_con_cualquier_creador(self) -> None:
        for logistica in self.creadores:
            with self.subTest(creador=type(logistica).__name__):
                with redirect_stdout(io.StringIO()):
                    resultado = logistica.planificar_entrega("Bogotá")
                self.assertIn("Bogotá", resultado)

    def test_logistica_maritima_reutiliza_el_mismo_barco(self) -> None:
        logistica = LogisticaMaritima()
        primero = logistica.crear_transporte()
        segundo = logistica.crear_transporte()
        self.assertIs(primero, segundo)

    def test_logistica_no_se_puede_instanciar(self) -> None:
        with self.assertRaises(TypeError):
            Logistica()  # type: ignore[abstract]


if __name__ == "__main__":
    unittest.main()
