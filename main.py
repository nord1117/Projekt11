"""
projekt_1.py: první projekt do Engeto
author: Táňa Silberová
"""
# Registrovaní uživatelé 
registrovani = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# Přihlášení 
uzivatel = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")
# Kontrola 
if uzivatel in registrovani and registrovani[uzivatel] == heslo:
    print("-" *40)
    print("Vítej v aplikaci," ,uzivatel, ". Máme 3 texty k analýze.")
    print("-" *40)
else:
    print("Neregistrovaný uživatel, ukončení programu.")
    quit() # ukončení programu
# Seznam textů
Texty = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
# Výber textu 
vyber = input("Vyberte číslo textu(1-3): ")
# Kontrola, zda je vstup číslo
if not vyber.isdigit():
        print("Chyba: Musíš zadat číslo")
        quit() # ukončení programu
cislo_textu = int(vyber)
# Kontrola rozsahu
if cislo_textu < 1 or cislo_textu > len(Texty):
        print("Chyba: Číslo mimo rozsah")
        quit() # ukončení programu
print("Vybral jsi text číslo", cislo_textu)
print("-" *40)
# Analýza textu
# Příprava slov (očištění od teček a čárek)
slova = []
for slovo in Texty[cislo_textu - 1].split():
    slova.append(slovo.strip(",."))

# Inicializace počítadel
title_case = 0
upper_case = 0
lower_case = 0
numeric = 0
suma_cisel = 0
delky_slov = {}
# Analýza slov
for slovo in slova:
    if slovo.istitle():
        title_case += 1
    elif slovo.isupper() and slovo.isalpha():
        upper_case += 1
    elif slovo.islower():
        lower_case += 1
    elif slovo.isdigit():
        numeric += 1
        suma_cisel += int(slovo)
    
    # Statistiky pro graf (délka slova)
    delka = len(slovo)
    delky_slov[delka] = delky_slov.get(delka, 0) + 1

# Výpis výsledků
print(f"Celkem slov: {len(slova)}")
print(f"Slov začínajících velkým písmenem: {title_case}")
print(f"Slov psaných velkými písmeny: {upper_case}")
print(f"Slov psaných malými písmeny: {lower_case}")
print(f"Počet čísel: {numeric}")
print(f"Součet všech čísel: {suma_cisel}")
print("-" * 40)
# Sloupcový graf
print(f"{'DÉLKA':<5}| {'VÝSKYT':<15} |{'POČET'}")
print("-" * 40)

for delka in sorted(delky_slov):
    hvezdicky = "*" * delky_slov[delka]
    print(f"{delka:<5}| {hvezdicky:<15} |{delky_slov[delka]}")
