# Piskvorky
from random import randrange
from random import choice

def vyhodnot(pole):
    # Funkce vrací jednoznakový řetězec podle stavu hry

    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):
#     "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    pred = pole[:cislo_policka]
    po = pole[cislo_policka+1:]
    return pred+symbol+po

def tah_hrace(pole):
    # Zaznamená do hry tah daného hráče
    cislo_policka = -1
    symbol = "x"
    while cislo_policka not in range(20) or pole[cislo_policka] != "-":
        cislo_policka = int(input("Na kterou pozici chceš umístit svůj symbol?:"))
        if cislo_policka in range(20) and pole[cislo_policka] == "-":
            pole = tah(pole, cislo_policka, symbol)
            return pole 
        else: 
            print("Tak takhle to nepůjde, zkus to znovu:")      


def tah_pocitace(pole):
    # Zaznamená do hry tah počítače (snaží se hrát vedle značky soupeře)
    cislo_policka = -1
    symbol = "o"
    while cislo_policka not in range(20) or pole[cislo_policka] != "-":
        if pole.find("-x") == -1 and pole.find("x-") == -1:
            cislo_policka = randrange(20)
        elif pole.find("-x") > -1 and pole.find("x-") > -1:
            cislo_policka = choice([pole.index("-x"),pole.index("x-")+1])
        elif pole.find("-x") == -1:
            cislo_policka = pole.index("x-")+1
        else:
            cislo_policka = pole.index("-x")

        if pole[cislo_policka] == "-":
            pole = tah(pole, cislo_policka, symbol)
            return pole   
               

def piskvorky1d():
    # Hraje hru piškvorky (hráč x počítač)
    pole = 20 * "-"
    print(pole)

    while  vyhodnot(pole) == "-":

        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != "x":
            pole = tah_pocitace(pole)
            print(pole)
        if vyhodnot(pole) == "x":
            print("Gratuluji!Vyhrál jsi!")
        elif vyhodnot(pole) == "o":
            print("Vyhrál počítač")


#test
piskvorky1d()