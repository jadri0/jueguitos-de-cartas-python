# jueguitos-de-cartas-python

Un juego sencillo de cartas escrito en Python. Un pequeño proyecto que comencé para empezar a familiarizarme con la programación orientada a objetos y para aprender a escribir e importar mis propios módulos y paquetes.
El objetivo del juego es adivinar correctamente una serie de condiciones relacionadas con cuatro cartas seleccionadas aleatoriamente de un mazo de 48 naipes de la baraja española.

## Cómo jugar

- Ronda 1: ¿El número de la carta es **par o impar**?
- Ronda 2: ¿La siguiente carta es **mayor o menor** que la anterior? En caso de que sean iguales, se considera mayor.
- Ronda 3: ¿La tercera carta está **dentro o fuera** del rango de las dos anteriores? Si la carta es igual a cualquiera de las dos anteriores, se considera que está dentro.
- Ronda 4: Adivina el **palo** de la cuarta carta (oros, copas, bastos o espadas).

## Uso

```bash
python main.py
```

## Requisitos

No se necesitan paquetes externos, solo Python 3.x.

## Estructura del Proyecto

- `adivina-la-carta/main.py` - Script principal
- `adivina-la-carta/utils/baraja.py` - Lógica de baraja y cartas
- `adivina-la-carta/utils/utils.py` - Utilidades como limpiar consola o salir
