# Gestión logística con Factory Method

Implementación en Python del patrón **Factory Method** basada en el ejemplo de logística de
[refactoring.guru](https://refactoring.guru/es/design-patterns/factory-method).

Requiere Python 3.10 o superior. No usa dependencias externas.

## Estructura

| Archivo | Rol en el patrón |
|---|---|
| `logistica/transporte.py` | Producto: interfaz abstracta `Transporte` |
| `logistica/transportes_concretos.py` | Productos concretos: `Camion`, `Barco`, `Avion` |
| `logistica/logistica.py` | Creadora: clase abstracta `Logistica` (`crear_transporte()`, `planificar_entrega()`) |
| `logistica/logisticas_concretas.py` | Creadores concretos: `LogisticaTerrestre`, `LogisticaMaritima`, `LogisticaAerea` |
| `main.py` | Cliente: elige el creador según la configuración |
| `tests/test_logistica.py` | Pruebas con `unittest` |
| `alternativa_if_elif.py` | Versión sin el patrón, para comparar |

## Ejecución

```bash
python main.py                                   # terrestre, destino Bogotá
python main.py --modo maritima --destino Cartagena
python main.py --modo aerea --destino Leticia
```

Pruebas:

```bash
python -m unittest -v
```

Versión alternativa:

```bash
python alternativa_if_elif.py --modo maritima
```

> En Windows, si las tildes se ven mal en la consola, agregar `-X utf8`
> (por ejemplo, `python -X utf8 main.py`).

## Extensión con transporte aéreo (Actividad 3.5)

| Archivo | Cambio |
|---|---|
| `logistica/transportes_concretos.py` | Se agregó la clase `Avion` |
| `logistica/logisticas_concretas.py` | Se agregó la clase `LogisticaAerea` |
| `main.py` | Se agregó el import de `LogisticaAerea` y la entrada `"aerea"` en `CREADORES` |

Solo se agregaron clases nuevas: `transporte.py` y `logistica.py` no cambiaron, y tampoco
las clases `Camion` ni `Barco`.

## Reutilización de objetos (Actividad 3.6)

`LogisticaMaritima.crear_transporte()` guarda el primer `Barco` creado y lo devuelve en las
llamadas siguientes. La prueba `test_logistica_maritima_reutiliza_el_mismo_barco` verifica
que se obtiene la misma instancia.

## Contraste con if/elif (Actividad 3.8)

| Criterio | if/elif en el cliente | Factory Method |
|---|---|---|
| Acoplamiento | Alto: el cliente conoce y crea cada clase concreta | Bajo: el cliente y `Logistica` solo conocen las interfaces |
| Agregar `Avion` | Modificar el `if/elif`, los `choices` y la función del cliente | Agregar dos clases nuevas y registrar una línea en la configuración |
| Cantidad de clases | 2 (una por transporte) | 6 con terrestre y marítimo (interfaz, creadora, 2 productos, 2 creadores); `Avion` suma 2 más |

La versión con `if/elif` es más corta, pero cada nuevo transporte obliga a modificar código que
ya funciona. Factory Method requiere más clases, a cambio de poder extenderse sin tocar el
código existente.
