from array import *
from Funktionen import *

Gewonnen = 0
CharP1 = ""
CharP2 = ""
Null = " . "
AktiSpi = 1

F = [[Null,Null,Null,Null,Null,Null,Null],
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

while (Gewonnen == 0):
    row, NaechstSpi  = ZugSpieler(AktiSpi)
    if (RepresentsInt(row) == True):
        Fn = Add_Chip(row, CharAktiSpie(AktiSpi, CharP1, CharP2), F, Null)
        F = Fn
        CheckWin(F, CharAktiSpie(AktiSpi, CharP1, CharP2))
    AktiSpi = NaechstSpi

