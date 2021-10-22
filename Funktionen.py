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
    CharP1, CharP2 = "  ", "  "
    while (CharP1 == "  " or CharP1 == "   " or CharP1 == Null):
        os.system('cls')
        print ("Sie können sich ihren Charakter auswählen. Gültig sind alle auf der Tastatur bis auf das Leerzeichen und der Punkt.")
        print ("Spieler 1, bitte Charakter wählen:")
        CharP1 = " " + input() + " "
    while (CharP2 == "  " or CharP2 == "   " or CharP2 == Null or CharP2 == CharP1):
        os.system('cls')
        print ("Sie können sich ihren Charakter auswählen. Gültig sind alle auf der Tastatur bis auf das Leerzeichen und der Punkt.")
        print ("Ausserdem sollte er nicht der selbe sein, wie bei Spieler 1")
        print ("Spieler 2, bitte Charakter wählen:")
        CharP2 = " " + input() + " "
    return CharP1, CharP2

def Add_Chip(Spalte, char, Feld, Null):
    chip_set = 0
    i = 0
    while (chip_set == 0):
        if (Feld[0][Spalte] != Null):
            print ("Diese Spalte ist schon voll")
            return Feld
        if (Feld[i][Spalte] != Null):
            Feld[i-1][Spalte] = char
            chip_set = 1
            AktiReihe = i - 1
            Print_Feld(Feld)
            return Feld, Spalte, AktiReihe
        else:
            i = i+1
        
def ZugSpieler(AktSpi):
    
    print ("Spieler", AktSpi, "ist drann. Wähle ein Feld")
    Spalte = input()
    if (RepresentsInt(Spalte) == True):
        Spalte = int(Spalte) - 1
        if(0 <= Spalte <= 6):
            if (AktSpi == 1):
                NaechstSpi = 2
            if (AktSpi == 2):
                NaechstSpi = 1
            return Spalte, NaechstSpi
        else:
            print("Das ist kein Feld, Wähle ein anderes")
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

def CheckWin(Feld, CharAktiSpi, AktiSpalte, AktiReihe):
    
    WinFlag = 0

    WinFlag = WaagCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi)
    
    if (WinFlag == 0):
        WinFlag = SenkCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi)
    
    if (WinFlag == 0):
        WinFlag = ULORQuerCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi)

    if(WinFlag == 0):
        WinFlag = OLURQuerCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi)

    return WinFlag

def WaagCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi):
    CheckFlag = 0
    WinFlag = 0
    while (CheckFlag == 0): # Check nach Links
        if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe][AktiSpalte - 1] == CharAktiSpi):
            AktiSpalte = AktiSpalte - 1
            WinFlag = WinFlag + 1
            if (WinFlag >= 3):
                return 1
        else:
            CheckFlag = 1

    WinFlag = 0
    while (CheckFlag == 1): # Check nach Rechts
        if(AktiSpalte < 6):
            if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe][AktiSpalte + 1] == CharAktiSpi):
                AktiSpalte = AktiSpalte + 1
                WinFlag = WinFlag + 1
                if (WinFlag >= 3):
                    return 1
            else:
                CheckFlag = 2
                return 0
        else:
            return 0

def SenkCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi):
    CheckFlag = 0
    WinFlag = 0
    while (CheckFlag == 0): # Check nach Unten
        if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe - 1][AktiSpalte] == CharAktiSpi):
            AktiReihe = AktiReihe - 1
            WinFlag = WinFlag + 1
            if (WinFlag >= 3):
                return 1
        else:
            CheckFlag = 1

    WinFlag = 0
    while (CheckFlag == 1): # Check nach Oben
        if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe + 1][AktiSpalte] == CharAktiSpi):
            AktiReihe = AktiReihe + 1
            WinFlag = WinFlag + 1
            if (WinFlag >= 3):
                return 1
        else:
            CheckFlag = 2
            return 0

def ULORQuerCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi):
    CheckFlag = 0
    WinFlag = 0
    while (CheckFlag == 0): # Check nach Unten Links
        if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe - 1][AktiSpalte - 1] == CharAktiSpi):
            AktiReihe = AktiReihe - 1
            AktiSpalte = AktiSpalte - 1
            WinFlag = WinFlag + 1
            if (WinFlag >= 3):
                return 1
        else:
            CheckFlag = 1

    WinFlag = 0
    while (CheckFlag == 1): # Check nach Oben Rechts
        if(AktiSpalte < 6):
            if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe + 1][AktiSpalte + 1] == CharAktiSpi):
                AktiReihe = AktiReihe + 1
                AktiSpalte = AktiSpalte + 1
                WinFlag = WinFlag + 1
                if (WinFlag >= 3):
                    return 1
            else:
                CheckFlag = 2
                return 0
        else:
            return 0

def OLURQuerCheck(Feld, AktiReihe, AktiSpalte, CharAktiSpi):
    CheckFlag = 0
    WinFlag = 0
    while (CheckFlag == 0): # Check nach Unten Rechts
        if(AktiSpalte < 6):
            if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe - 1][AktiSpalte + 1] == CharAktiSpi):
                AktiReihe = AktiReihe - 1
                AktiSpalte = AktiSpalte + 1
                WinFlag = WinFlag + 1
                if (WinFlag >= 3):
                    return 1
            else:
                CheckFlag = 1
        else:
            return 0

    WinFlag = 0
    while (CheckFlag == 1): # Check nach Oben Link363
        if(AktiSpalte < 6):
            if (Feld[AktiReihe][AktiSpalte] == CharAktiSpi and Feld[AktiReihe + 1][AktiSpalte - 1] == CharAktiSpi):
                AktiReihe = AktiReihe + 1
                AktiSpalte = AktiSpalte - 1
                WinFlag = WinFlag + 1
                if (WinFlag >= 3):
                    return 1
            else:
                CheckFlag = 2
                return 0
        else:
            return 0