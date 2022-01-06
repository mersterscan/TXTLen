# Vared Kardan Library Haye Mored Niaz !

from os import system as Run

try:
    from colorama import Fore as TextColor
except:
    Run("pip3 install colorama")
    from colorama import Fore as TextColor
    
try:
    from time import sleep as Wait
except:
    Run("pip3 install time")
    from time import sleep as Wait
    
Run("cls" or "clear")

# <---------------------------------------/>

# Tozihat Barname

print(TextColor.LIGHTCYAN_EX + "<--------------------------------------------------------> \n\n [</>]: Be Barname Shomaresh Horoof TXT Khosh Umadid Dust Khubam :) \n\n [!]: Tavajoh Konid Lotfan Dar Vared Kardan Adress File TXT Besyar Deghat Konid ! Dar Paiin Mesali Amade Ast:\n\n [Example]: C:/Users/MesterScan/Desktop/MyTXT.txt \n\n <------------------------------------------------------/>")

# Daryaft Maghadir

Loc = input(TextColor.LIGHTMAGENTA_EX + "\n\n[/]: Lotfan Adress File TXT Khod Ra Manand Mesal Vared Konid -->> ")

Soal = input(TextColor.LIGHTRED_EX + "\n\n[?]: Aya Space Haro Ham Hesab Konam ? [ N / Y ] --> ").lower()

# Baz Kardan File Va Mohasebat

Count = 0

File = open(Loc , "r")

Text = f"{str(File.read())}"

for Harf in Text:
    if Soal == 'n':
        
        if Harf == " ":
            pass
        else:
            Count = Count + 1
    if Soal == 'y':
        Count = Count + 1

# Bazgasht Etelaat File

print(TextColor.LIGHTGREEN_EX + f"\n[-]: Dar File TXT Shoma {Count} Harf Peyda Shod !\n\n[$]: @MesTerScan")

input(TextColor.BLUE + "\n[Exit]: Dokme Enter Ra Baraye Khorooj Feshar Dahid")