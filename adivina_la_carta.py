import random
import baraja_es as naipes
import exit_reset as exit

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
    if fin == "salir":
        raise KeyboardInterrupt
    if fin == "reset":
        main()

def par_o_impar():
    while True:
        input_par = input("¿Par o impar?: ").strip().lower()
        print("")
        if carta1.number % 2 == 0:
            es_par = True
        else:
            es_par = False
        if input_par == "par":
            if es_par == True:
                print(carta1,"\n")
                break
            else:
                print(carta1,"\n\nHas perdido...")
                fin()
        elif input_par == "impar":
            if es_par == False:
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
        if carta2.number >= carta1.number:
            es_mayor = True
        else:
            es_mayor = False
        if input_mayor == "mayor":
            if es_mayor == True:
                print(carta2,"\n")
                break
            else:
                print(carta2,"\n\nHas perdido...")
                fin()
        elif input_mayor == "menor":
            if es_mayor == False:
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
        if carta3.number in range(cartas_num[0],cartas_num[1] + 1):
            esta_dentro = True
        else:
            esta_dentro = False
        if input_dentro == "dentro":
            if esta_dentro == True:
                print(carta3,"\n")
                break
            else:
                print(carta3,"\n\nHas perdido...")
                fin()
        elif input_dentro == "fuera":
            if esta_dentro == False:
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
            elif input_palo != carta4.suit:
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