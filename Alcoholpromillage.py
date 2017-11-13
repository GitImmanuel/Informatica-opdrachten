import math
import time
import sys

#informatie ophalen
def informatieophalen():
    global geslacht, gewicht, uren, glazen
    def gewichtfunctie():
        try:
            global gewicht
            gewicht = int(input('Vul je gewicht in in kg: '))
            print('')
        except ValueError:
            print(' ')
            print('Vul alstublieft een getal in.')
            gewichtfunctie()

    gewichtfunctie()

    def glazenfunctie():
        try:
            global glazen
            glazen = int(input('Vul nu in hoeveel glazen je hebt gedronken: '))
            print('')
        except ValueError:
            print(' ')
            print('Vul alstublieft een getal in.')
            glazenfunctie()

    glazenfunctie()

    geslacht = input('Vul je geslacht in (man, vrouw of overige): ')
    print(' ')

    def urenfunctie():
        try:
            global uren
            uren = int(input('Vertel ons hoeveel uur het geleden is dat je je laatste glas hebt gedronken: '))
            print('')
        except ValueError:
            print(' ')
            print('Vul alstublieft een getal in.')
            urenfunctie()

    urenfunctie()

informatieophalen()

#rekenen
alcoholprom = int(glazen) * 10

#rekenen
urenreken = uren - 0.5
gewichtreken = gewicht * 0.002
alcoholpromlaatst = urenreken * gewichtreken

#Rekenen
ovv = int(gewicht) * 0.6
vrouww = int(gewicht) * 0.5
mann = int(gewicht) * 0.7

#Bepalen welk geslacht + rekenen
if geslacht == "man" or geslacht == "m":
    alcoholman = int(alcoholprom) / mann
    vocht = 0.7
    alcoholpromillage = alcoholman - alcoholpromlaatst
    geslacht = 'man,'
    
elif geslacht == "vrouw" or geslacht == 'v':
    alcoholvrouw = int(alcoholprom) / vrouww
    vocht = 0.5
    alcoholpromillage = alcoholovrouw - alcoholpromlaatst
    geslacht = 'vrouw,'
    
else:
    alcoholoverige = int(alcoholprom) / ovv
    vocht = 0.6
    alcoholpromillage = alcoholoverige - alcoholpromlaatst
    geslacht = 'overige,'
print(' ')

#Mooie tekst    
print('Je gewicht is', gewicht,'kg.')
time.sleep(1)
print(' ')
print('Je hebt', glazen, 'glas(zen) gedronken.')
time.sleep(1)
print(' ')
print('Je bent een', geslacht, 'dus je lichaamsvocht is ongeveer', vocht)
time.sleep(1.5)
print(' ')
print('Je hebt', uren, 'uur geleden je laatste glas gedronken.')
time.sleep(1.5)
print(' ')

print('Nu gaan we rekenen')
time.sleep(.8)
text = "     "
for char in text:
    sys.stdout.write(char)
    time.sleep(0.7)


print(' ')


print('Je alcoholpromillage is', alcoholpromillage, 'mooi, we kunnen verder.')
time.sleep(1.8)
print(' ')

#Uiteindelijk antwoord
if -5 < alcoholpromillage < 0.5:
    print('Je toestand is opgewekt! Valt mee dus.')
elif 0.5 < alcoholpromillage < 1.5:
    print('Je toestand is aangeschoten! Dat valt mee.')
    
elif 1.5 < alcoholpromillage < 3.0:
    print('Je toestand is zat! Je hebt aardig wat gedronken.')

elif 3.0 < alcoholpromillage < 4.0:
    print('Je toestand is ladderzat! Je hebt veel gedronken.')

elif 4.0 < alcoholpromillage < 100000:
    print('Je toestand is laveloos! Let op met hoeveel je drinkt!')

time.sleep(1.8)
print(' ')

#OPDRACHT 2-------------------------------------------------------------

if alcoholpromillage < 0.2:
    hoag = 'goed om te rijden.'
elif 0.2 < alcoholpromillage:
    hoag = 'te hoog om te rijden! Ga niet de weg op.'

print("Je mag niet rijden vanaf een alcoholpromillage van 0,2. Uw alcoholpromillage is", hoag, 'Let altijd goed op terwijl je rijdt, ook nuchter!')
time.sleep(4)
print(' ')

print('Er wordt gezegd dat je na 3 biertjes absoluut niet meer achter het stuur mag, dit is meestal waar maar het ligt aan uw gewicht en hoelang het geleden is.')
time.sleep(6)
print(' ')

print('!!!DISCLAIMER!!! GA NOOIT MET ALCOHOL OP ACHTER HET STUUR!')
print(' ')
time.sleep(3)

def wachten():
    for nieuw in range(1, 250):
        nieuweuren = nieuw - 0.5
        abaaa = nieuweuren * gewichtreken
        if geslacht == "man,":
            probeer = alcoholman - abaaa
            if probeer == 0.2 or probeer < 0.2:
                haha = nieuw - uren
                print("Je mag na", haha, "uur weer rijden!")
                break
        elif geslacht == "vrouw,":
            probeer = alcoholvrouw - abaaa
            if probeer == 0.2 or probeer < 0.2:
                haha = nieuw - uren
                print("Je mag na", haha, "uur weer rijden!")
                break
        else:
            probeer = alcoholoverige - abaaa
            if probeer == 0.2 or probeer < 0.2:
                haha = nieuw - uren
                print("Je mag na", haha, "uur weer rijden!")
                break

wachten()

print('')


input('Exit the terminal when done')
