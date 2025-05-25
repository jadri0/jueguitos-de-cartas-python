import random
from utils import baraja_es
from utils import baraja_fr
from utils import exit_reset as exre
from utils import card_printer as pr

def sacar_cartas():
    global carta1, carta2, carta3, carta4, baraja
    while True:   
        baraja = input("¿Con qué baraja quieres jugar?\n\n[e]spañola      [f]rancesa\n\n").strip().lower()
        if baraja in ["e", "es", "españa", "española", "español"]:
            baraja = baraja_es
            while True:
                carta1 = random.choice(baraja_es.deck)
                carta2 = random.choice(baraja_es.deck)
                carta3 = random.choice(baraja_es.deck)
                carta4 = random.choice(baraja_es.deck)
                lista_cartas = [carta1, carta2, carta3, carta4]
                if len(lista_cartas) == len(set(lista_cartas)):
                    break
            break
        elif baraja in ["f", "fr", "francia", "francesa", "frances", "francés"]:
            baraja = baraja_fr
            while True:
                carta1 = random.choice(baraja_fr.deck)
                carta2 = random.choice(baraja_fr.deck)
                carta3 = random.choice(baraja_fr.deck)
                carta4 = random.choice(baraja_fr.deck)
                lista_cartas = [carta1, carta2, carta3, carta4]
                if len(lista_cartas) == len(set(lista_cartas)):
                    break
            break
        else:
            print("\nCreo que no te he entendido bien...\n")

def fin():
    fin = input("\n[s]alir      [r]eset\n\n").strip().lower()
    if fin in ["r", "reset"]:
        main()
    if fin in ["s", "salir"]:
        exre.exit()
    else:
        raise KeyboardInterrupt

def par_o_impar():
    while True:
        input_par = input("\n¿Par o impar?: ").strip().lower()
        print("")
        es_par = carta1.number % 2 == 0
        if input_par in ["p", "par"]:
            if es_par:
                pr.print_card(carta1)
                print(carta1,"\n")
                break
            else:
                pr.print_card(carta1)
                print(carta1,"\n\nHas perdido...")
                fin()
        elif input_par in ["i", "impar"]:
            if not es_par:
                pr.print_card(carta1)
                print(carta1,"\n")
                break
            else:
                pr.print_card(carta1)
                print(carta1,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...")

def mayor_o_menor():
    while True:
        input_mayor = input("¿Mayor o menor?: ").strip().lower()
        print("")
        es_mayor = carta2.number >= carta1.number
        if input_mayor in ["ma", "may", "mayor", ">"]:
            if es_mayor:
                pr.print_card(carta2)
                print(carta2,"\n")
                break
            else:
                pr.print_card(carta2)
                print(carta2,"\n\nHas perdido...")
                fin()
        elif input_mayor in ["me", "men", "menor", "<"]:
            if not es_mayor:
                pr.print_card(carta2)
                print(carta2,"\n")
                break
            else:
                pr.print_card(carta2)
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
        if input_dentro in ["d", "dentro"]:
            if esta_dentro:
                pr.print_card(carta3)
                print(carta3,"\n")
                break
            else:
                pr.print_card(carta3)
                print(carta3,"\n\nHas perdido...")
                fin()
        elif input_dentro in ["f", "fuera"]:
            if not esta_dentro:
                pr.print_card(carta3)
                print(carta3,"\n")
                break
            else:
                pr.print_card(carta3)
                print(carta3,"\n\nHas perdido...")
                fin()
        else:
            print("Creo que no te he entendido bien...\n")

def palo():
    if baraja == baraja_es:
        while True:
            palos = ["oros", "copas", "espadas", "bastos"]
            iniciales = ["o", "c", "e", "b"]
            input_palo = input("¿Palo?: ").strip().lower()
            print("")
            if input_palo in iniciales:
                input_palo = palos[iniciales.index(input_palo)]
            if input_palo in palos:
                if input_palo == carta4.suit:
                    pr.print_card(carta4)
                    break
                else:
                    pr.print_card(carta4)
                    print(carta4,"\n\nHas perdido...")
                    fin()
            else:
                print("Creo que no te he entendido bien...\n")
    if baraja == baraja_fr:
        palos = ["picas", "corazones", "diamantes", "tréboles"]
        iniciales = ["p", "c", "d", "t"]
        while True:
            input_palo = input("¿Palo?: ").strip().lower()
            print("")
            if input_palo == "treboles":
                input_palo = "tréboles"
            elif input_palo in iniciales:
                input_palo = palos[iniciales.index(input_palo)]
            if input_palo in palos:
                if input_palo == carta4.suit:
                    pr.print_card(carta4)
                    break
                else:
                    pr.print_card(carta4)
                    print(carta4,"\n\nHas perdido...")
                    fin()
            else:
                print("Creo que no te he entendido bien...\n")

def main():
    try:
        exre.clear()
        print("¡Adivina la carta!\n\n"
              "Ronda 1: [p]ar o [i]mpar\n"
              "Ronda 2: [ma]yor o [me]nor (si el número de la segunda carta es igual al de la primera, se considera mayor)\n"
              "Ronda 3: [d]entro o [f]uera (si el número de la carta es igual al de alguna de las dos cartas anteriores, se considera dentro)\n" \
              "Ronda 4: palo\nBaraja española: [o]ros [c]opas [e]spadas [b]astos\nBaraja francesa: [p]icas [c]orazones [d]iamantes [t]réboles\n")
        sacar_cartas()
        par_o_impar()
        mayor_o_menor()
        dentro_o_fuera()
        palo()
        print("¡Has ganado!")
        fin()
    except KeyboardInterrupt:
        exre.keyboard_exception()

main()