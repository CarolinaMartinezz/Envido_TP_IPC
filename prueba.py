import random

# Mazo
mazo_cartas = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E10", "E11", "E12",
                "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B10", "B11", "B12",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C10", "C11", "C12",
                "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O10", "O11", "O12"]

valores_mazo_general = {
    "E1": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6, "E7": 7, "E10": 0, "E11": 0, "E12": 0,
    "B1": 1, "B2": 2, "B3": 3, "B4": 4, "B5": 5, "B6": 6, "B7": 7, "B10": 0, "B11": 0, "B12": 0,
    "C1": 1, "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C10": 0, "C11": 0, "C12": 0,
    "O1": 1, "O2": 2, "O3": 3, "O4": 4, "O5": 5, "O6": 6, "O7": 7, "O10": 0, "O11": 0, "O12": 0
}
#manos = random.sample(mazo_cartas , 6)
mazo_jugador= random.sample(mazo_cartas, 3) #creo el mazo del jugador y elimino las cartas del mazo principal
for carta_usada in mazo_jugador:
    mazo_cartas.remove(carta_usada)

mazo_comp= random.sample (mazo_cartas, 3) #creo el mazo de la computadora y elimino las cartas del mazo principal
for carta_usada in mazo_comp:
    mazo_cartas.remove(carta_usada)

#calculo valor del mazo
valor_jugador= sum(valores_mazo_general[valor] #indico de donde tiene que sacar el valor
                   for valor in mazo_jugador)  #indico que cartas aplican a la suma

valor_comp= sum (valores_mazo_general[valor]   #indico de donde tiene que sacar el valor
                 for valor in mazo_comp)       #indico que cartas aplican a la suma



print (mazo_jugador)
print (mazo_comp)
print ('valor jugador:', valor_jugador)
print ('valor_comp:', valor_comp)