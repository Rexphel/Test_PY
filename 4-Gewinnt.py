from array import *
from Funktionen import *

WinFlag = 0
CharP1 = ""
CharP2 = ""
Null = " . "
AktiSpi = 1

F = [[Null,Null,Null,Null,Null,Null,Null],
    [Null,Null,Null,Null,Null,Null,Null],
    [Null,Null,Null,Null,Null,Null,Null],
    [Null,Null,Null,Null,Null,Null,Null],
    [Null,Null,Null,Null,Null,Null,Null],
    [Null,Null,Null,Null,Null,Null,Null],
    [" ^ "," ^ "," ^ "," ^ "," ^ "," ^ "," ^ "],
    [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "]
    ]

Start()

CharP1, CharP2 = GetChars(Null)
Print_Feld(F)

while (WinFlag == 0):
    AktiSpalte, NaechstSpi  = ZugSpieler(AktiSpi)
    if (RepresentsInt(AktiSpalte) == True):
        Fn, AktiReihe, AktiSpalte = Add_Chip(AktiSpalte, CharAktiSpie(AktiSpi, CharP1, CharP2), F, Null)
        F = Fn
        WinFlag = CheckWin(F, CharAktiSpie(AktiSpi, CharP1, CharP2), AktiReihe, AktiSpalte)
    AktiSpi = NaechstSpi

print("LOL WIN")