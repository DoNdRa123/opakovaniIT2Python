import random

# Funkce pro hod kostkou
def hod_kostkou():
    return random.randint(1, 6)

# Funkce pro hru
def hra():
    
    pocet_hracu = int(input("Zadejte počet hráčů: "))
    
    skore = [0] * pocet_hracu
   
    kostky_hodnoty = [[0] * 3 for _ in range(pocet_hracu)]

    
    for kolo in range(7):
        print(f"\nKolo {kolo + 1}")
        for hrac in range(pocet_hracu):
            print(f"\nHráč {hrac + 1}")
            
            for hod in range(3):
                print(f"Hod {hod + 1}:")
                hodnoty = [hod_kostkou() for _ in range(3)]
                kostky_hodnoty[hrac] = hodnoty
                print(f"Hodil jsi {hodnoty}")
                
                opakovat = input("Chcete házet znovu? (ano/ne): ").lower()
                if opakovat == "ne":
                    break
                else:
                    
                    nechat_kostky = input("Zadejte čísla kostek, které si chcete nechat (např. '1 3'): ").split()
                    nechat_kostky = [int(i) - 1 for i in nechat_kostky]
                    zbytek_kostek = [i for i in range(3) if i not in nechat_kostky]
                    hodnoty = [hod_kostkou() for _ in zbytek_kostek] + [kostky_hodnoty[hrac][i] for i in nechat_kostky]
                    kostky_hodnoty[hrac] = hodnoty
                    print(f"Hodil jsi {hodnoty}")

            # Vypočítá se skóre hráče pro toto kolo
            kolo_skore = 0
            for hodnota in kostky_hodnoty[hrac]:
                if hodnota == 1:
                    kolo_skore += 100
                elif hodnota == 6:
                    kolo_skore += 60
                else:
                    kolo_skore += hodnota
            skore[hrac] += kolo_skore
            print(f"V tomto kole jsi získal {kolo_skore} bodů.\n")

    # Vypíše se konečné skóre
    print("\nKonečné skóre:")
    for i, hrac_skore in enumerate(skore):
        print(f"Hráč {i + 1}: {hrac_skore} bodů")

    # Vypíše se vítěz
    vitez = skore.index(max(skore)) + 1
    print(f"\nVítězem se stal hráč {vitez} s {max(skore)} body.")


hra()