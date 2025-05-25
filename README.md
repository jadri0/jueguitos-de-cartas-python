# jueguitos-de-cartas-python

Un juego sencillo de cartas escrito en Python. Un pequeño proyecto que comencé para empezar a familiarizarme con el uso de funciones y con la programación orientada a objetos, y también para aprender a escribir e importar mis propios módulos y paquetes, estructurando un proyecto de una manera más organizada y profesional.
El objetivo del juego es adivinar correctamente una serie de condiciones relacionadas con cuatro cartas seleccionadas al azar.
Se puede elegir jugar con la baraja española (de 48 naipes, con ochos y nueves) o con la francesa, y además, hay representación gráfica de las cartas mediante arte ASCII.

## Cómo jugar

- Elegir baraja: española o francesa.
- Ronda 1: ¿El número de la carta es **par o impar**? En la baraja francesa, al tener tanto 10 como J, la J y la K se consideran impares, mientras que la Q se considera par. La baraja española no tiene este problema, al ser completamente numérica.
- Ronda 2: ¿La siguiente carta es **mayor o menor** que la anterior? En caso de que sean iguales, se considera mayor.
- Ronda 3: ¿La tercera carta está **dentro o fuera** del rango de las dos anteriores? Si la carta es igual a cualquiera de las dos anteriores, se considera que está dentro.
- Ronda 4: Adivina el **palo** de la cuarta carta: oros, copas, bastos o espadas, en el caso de la baraja española; corazones, picas, diamantes y tréboles, en el caso de la francesa.

## Uso

```bash
python main.py
```
