import random
from utils import baraja as naipes
from utils import utils as exit

def sacar_cartas():
    global carta1, carta2, carta3, carta4
    while True:
        carta1 = random.choice(naipes.deck)
        carta2 = random.choice(naipes.deck)
        carta3 = random.choice(naipes.deck)
        carta4 = random.choice(naipes.deck)
        lista_cartas = [carta1, carta2, carta3, carta4]
        if len(lista_cartas) == len(set(lista_cartas)):
            break

def fin():
    fin = input("\n[salir]      [reset]\n\n").strip().lower()
    if fin == "reset":
        main()
    else:
        raise KeyboardInterrupt

def par_o_impar():
    while True:
        input_par = input("¿Par o impar?: ").strip().lower()
        print("")
        es_par = carta1.number % 2 == 0
        if input_par == "par":
            if es_par:
                print(carta1,"\n")
                break
            else:
                print(carta1,"\n\nHas perdido...")
                fin()
        elif input_par == "impar":
            if not es_par:
                print(carta1,"\n")
                break
            else:
                print(carta1,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...\n")

def mayor_o_menor():
    while True:
        input_mayor = input("¿Mayor o menor?: ").strip().lower()
        print("")
        es_mayor = carta2.number >= carta1.number
        if input_mayor == "mayor":
            if es_mayor:
                print(carta2,"\n")
                break
            else:
                print(carta2,"\n\nHas perdido...")
                fin()
        elif input_mayor == "menor":
            if not es_mayor:
                print(carta2,"\n")
                break
            else:
                print(carta2,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...\n")

def dentro_o_fuera():
    while True:
        cartas_num = [carta1.number, carta2.number]
        cartas_num.sort()
        input_dentro = input("¿Dentro o fuera?: ").strip().lower()
        print("")
        esta_dentro = carta3.number in range(cartas_num[0], cartas_num[1] + 1)
        if input_dentro == "dentro":
            if esta_dentro:
                print(carta3,"\n")
                break
            else:
                print(carta3,"\n\nHas perdido...")
                fin()
        elif input_dentro == "fuera":
            if not esta_dentro:
                print(carta3,"\n")
                break
            else:
                print(carta3,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...\n")

def palo():
    while True:
        palos = ["oros", "copas", "espadas", "bastos"]
        input_palo = input("¿Palo?: ")
        print("")
        if input_palo in palos:
            if input_palo == carta4.suit:
                break
            else:
                print(carta4,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...\n")

def main():
    try:
        exit.clear()
        sacar_cartas()
        print("¡Adivina la carta!\n\n"
              "Ronda 1: [Par] o [impar]\n"
              "Ronda 2: [Mayor] o [menor] (si el número de la segunda carta es igual al de la primera, se considera mayor)\n"
              "Ronda 3: [Dentro] o [fuera] (si el número de la carta es igual al de alguna de las dos cartas anteriores, se considera dentro)\n" \
              "Ronda 4: Palo [oros] [copas] [espadas] [bastos]\n")
        par_o_impar()
        mayor_o_menor()
        dentro_o_fuera()
        palo()
        print("¡Has ganado!")
        fin()
    except KeyboardInterrupt:
        exit.keyboard_exception()

main()