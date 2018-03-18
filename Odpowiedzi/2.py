# -*- coding: utf8 -*-

"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i jego oceny.
Dodaj do swojego spisu.
"""
serials = {
    'Reign' : 7.8,
    'Game of Thrones' : 8.5,
    'Anne with an E' : 8.1,
    'Peaky Blinders' : 8.7,
    'The Big Bang Theory' : 8,
    'Riverdale' : 7.3,
    'Lucyfer': 8,
    "The Handmaid's Tale" : 8.1,
    'Jessica Jones' : 8.4,
    'La casa de papel' : 7.8
    }

print(list(serials.keys()))
print('******************************************')

name = input('Jaki serial chcesz obejrzec? ')
print("Serial {} otrzymał ocenę {}".format(name, serials[name]))

print('******************************************')
new = input('Jaki serial dodać do bazy? ')
rating = input('Jaką ocenę otrzymał ' + new + '? ')
serials[new] = float(rating)

print('******************************************')
print(list(serials.keys())) 
    
