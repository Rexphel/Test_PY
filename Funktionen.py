import os

def Start():
    
    print ("Willkommen bei 4 Gewinnt :D")
    print ("Klicke eine Taste um fort zu fahren")
    input()
    os.system('cls')

def Print_Feld(F):
    os.system('cls')
    for r in F:
        for c in r:
            print(c,end = "|")
        print()

def GetChars(Null):
    CharP1, CharP2 = " ", " "
    while (CharP1 == "" or CharP1 == " " or CharP1 == Null):
        os.system('cls')
        print ("Sie können sich ihren Charakter auswählen. Gültig sind alle auf der Tastatur bis auf das Leerzeichen und der Punkt.")
        print ("Spieler 1, bitte Charakter wählen:")
        CharP1 = " " + input() + " "
    while (CharP2 == "" or CharP2 == " " or CharP2 == Null or CharP2 == CharP1):
        os.system('cls')
        print ("Sie können sich ihren Charakter auswählen. Gültig sind alle auf der Tastatur bis auf das Leerzeichen und der Punkt.")
        print ("Ausserdem sollte er nicht der selbe sein, wie bei Spieler 1")
        print ("Spieler 2, bitte Charakter wählen:")
        CharP2 = " " + input() + " "
    return CharP1, CharP2

def Add_Chip(row, char, Feld, Null):
    chip_set = 0
    i = 0
    while (chip_set == 0):
        if (Feld[0][row] != Null):
            print ("Diese Reihe ist schon voll")
            return Feld
        if (Feld[i][row] != Null):
            Feld[i-1][row] = char
            chip_set = 1
            Print_Feld(Feld)
            return Feld
        else:
            i = i+1
        
def ZugSpieler(AktSpi):
    
    print ("Spieler", AktSpi, "ist drann. Wähle ein Feld")
    row = input()
    if (RepresentsInt(row) == True):
        row = int(row) - 1
        if(0 <= row <= 6):
            if (AktSpi == 1):
                NaechstSpi = 2
            if (AktSpi == 2):
                NaechstSpi = 1
            return row, NaechstSpi
        else:
            print("Das ist kein Feld")
            return "A", AktSpi
    else:
        print("Das ist keine Zahl")
        return "A", AktSpi

def CharAktiSpie(AktiSpie, CharP1, CharP2):
    if (AktiSpie == 1):
        return CharP1
    if (AktiSpie == 2):
        return CharP2

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def CheckWin(Feld, CharAktiSpi):
    print("win")