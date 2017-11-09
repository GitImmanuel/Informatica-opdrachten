import math
import time
import sys

#Welkom
print('Welkom!')
print('')
time.sleep(0.5)

#Info ophalen
a = int(input('Vul eerst uw getal voor "a" in: '))
print(' ')

b = int(input('Vul nu uw getal voor "b" in: '))
print(' ')
c = int(input('Vul nu het getal voor "c" in: '))
print(' ')
time.sleep(0.5)

#Praten
print('U heeft voor a het getal', a)
print(' ')
time.sleep(1.2)
print('U heeft voor b het getal', b)
print(' ')
time.sleep(1.2)
print('U heeft voor c het getal', c)
print(' ')
time.sleep(1.2)

#Checken
klopt = input('Klopt dit? (ja of nee): ')
print(' ')
time.sleep(0.5)

#Functie
def functienaam():
    a = int(input('Vul uw getal voor "a" in: '))
    print(' ')
    b = int(input('Vul uw getal voor "b" in: '))
    print(' ')
    c = int(input('Vul het getal voor "c" in: '))
    print(' ')
    time.sleep(0.5)

    print('U heeft voor a het getal', a)
    print(' ')
    time.sleep(1.2)
    print('U heeft voor b het getal', b)
    print(' ')
    time.sleep(1.2)
    print('U heeft voor c het getal', c)
    print(' ')
    time.sleep(1.2)

    klopt = input('Klopt dit? (ja of nee): ')
    print(' ')
    time.sleep(0.5)

    if klopt == "j" or klopt == "ja":
        print('Mooi zo, we gaan verder!')
    else:
        functienaam();

#Checken
if klopt == "j" or klopt == "ja":
    print('Mooi zo, we gaan verder!')
    print('')
    time.sleep(0.8)
else:
    functienaam()

#Rekenen(D)
deel1D = b * b
deel2D = -4 * a * c
D = deel1D + deel2D

if D < 0:
    print('Er zijn geen oplossingen gevonden!')
    print('')
    time.sleep(1.2)

elif D == 0:
    print('Er is één oplossing gevonden!')
    print('')
    time.sleep(1.1)

    # Rekenen(x1)
    X1deel1 = -b + math.sqrt(D)
    X1deel2 = 2 * a
    X1 = X1deel1 / X1deel2

    print('De oplossing is:',X1)
    print('')
    time.sleep(1.1)

elif D > 0:
    print('Er zijn twee oplossingen gevonden!')
    print('')
    time.sleep(1.1)

    # Rekenen(x2)
    Formule2deel1 = -b - math.sqrt(D)
    Formule2deel2 = 2 * a
    Formule2 = Formule2deel1 / Formule2deel2

    # Rekenen(x1)
    X1deel1 = -b + math.sqrt(D)
    X1deel2 = 2 * a
    X1 = X1deel1 / X1deel2

    print('De oplossingen zijn', X1, 'en', Formule2)
    print('')
    time.sleep(1.1)

if a < 0:
    print('Je hebt te maken met een bergparabool!')
    print('')
    time.sleep(1.2)

    #Rekenen(x)
    x = -b / 2 * a
    yTop = a * (x * x) + b * x + c

    print('De top van de parabool is: ', yTop)

elif a > 0:
    print('Je hebt te maken met een dalparabool!')
    print('')
    time.sleep(1.2)

    #Rekenen(x)
    x = -b / 2 * a
    yTop = a * (x * x) + b * x + c

    print('De top van de parabool is: ', yTop)





input('Exit terminal when done')
