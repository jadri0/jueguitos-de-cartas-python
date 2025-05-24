# jueguitos-de-cartas-python

Un juego sencillo de cartas escrito en Python. El objetivo es adivinar correctamente una serie de condiciones relacionadas con una carta seleccionada aleatoriamente.

## Cómo jugar

1. Ronda 1: ¿El número de la carta es **par o impar**?
2. Ronda 2: ¿La siguiente carta es **mayor o menor** que la anterior?
3. Ronda 3: ¿La tercera carta está **dentro o fuera** del rango de las dos anteriores?
4. Ronda 4: Adivina el **palo** de la cuarta carta.

## Uso

```bash
python main.py
```

## Requisitos

No se necesitan paquetes externos, solo Python 3.x.

## Estructura del Proyecto

- `main.py` - Script principal
- `jueguitos/baraja.py` - Lógica de baraja y cartas
- `jueguitos/utils.py` - Utilidades como limpiar consola o salir