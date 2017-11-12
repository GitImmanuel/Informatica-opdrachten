import math
import time
import sys

#informatie ophalen
gewicht = int(input('Vul je gewicht in in kg: '))
print(' ')

glazen = int(input('Vul nu in hoeveel glazen je hebt gedronken: '))
print(' ')

geslacht = input('Vul je geslacht in (man, vrouw of overige): ')
print(' ')

uren = int(input('Vertel ons hoeveel uur het geleden is dat je je laatste glas hebt gedronken: '))
print(' ')

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

if -10 < alcoholpromillage < 0.2:
    hoag = 'goed om te rijden.'
elif  0.2 < alcoholpromillage:
    hoag = 'te hoog om te rijden! Ga niet de weg op.'
print("Je mag niet rijden vanaf een alcoholpromillage van 0,2. Uw alcoholpromillage is", hoag, 'Let altijd goed op terwijl je rijdt, ook nuchter!')
time.sleep(4)
print(' ')

print('Er wordt gezegt dat je na 3 biertjes absoluut niet meer achter het stuur mag, dit is meestal waar maar het ligt aan uw gewicht en hoelang het geleden is.')
time.sleep(6)
print(' ')

print('!!!DISCLAIMER!!! GA NOOIT MET ALCOHOL OP ACHTER HET STUUR!')
print(' ')
time.sleep(3)

if 0.2 < alcoholpromillage:
    print('Uw promillage is te hoog om te rijden, wacht nog even met rijden.')
    print(' ')
time.sleep(4)


for nieuw in range(3, 51):
    nieuweuren = nieuw - 0.5
    abaaa = nieuweuren * gewichtreken
    probeer = alcoholman - abaaa
    if probeer == 0.2 or probeer < 0.2:
        print("Je mag na", nieuw, "uur weer rijden!")
        break

print('')


input('Exit the terminal when done')
