import random

# Mazo
mazo_completo = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E10", "E11", "E12",
                "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B10", "B11", "B12",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C10", "C11", "C12",
                "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O10", "O11", "O12"]

# Mazo + valores.
valores_cartas = {
    "E1": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6, "E7": 7, "E10": 0, "E11": 0, "E12": 0,
    "B1": 1, "B2": 2, "B3": 3, "B4": 4, "B5": 5, "B6": 6, "B7": 7, "B10": 0, "B11": 0, "B12": 0,
    "C1": 1, "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C10": 0, "C11": 0, "C12": 0,
    "O1": 1, "O2": 2, "O3": 3, "O4": 4, "O5": 5, "O6": 6, "O7": 7, "O10": 0, "O11": 0, "O12": 0
}

# Iniciar mazos del jugador y de la computadora??
cartas_jugador = []
cartas_computadora = []

# Asignación de cartas al user.
while len(cartas_jugador) < 3:
    carta_index = random.randint(0, len(mazo_completo))
    carta = mazo_completo.pop(carta_index) #
    cartas_jugador += [carta]

# Asignación de cartas a la computadora
while len(cartas_computadora) < 3:
    carta_index = random.randint(0, len(mazo_completo))
    carta =mazo_completo.pop(carta_index)
    cartas_computadora += [carta]

# Valor total de cada mazo.
valor_total_jugador = sum(valores_cartas[carta] for carta in cartas_jugador)
valor_total_computadora = sum(valores_cartas[carta] for carta in cartas_computadora)

print("Cartas del jugador:", cartas_jugador)
print("Valor total del mazo del jugador:", valor_total_jugador)

print("Cartas de la computadora:", cartas_computadora)
print("Valor total del mazo de la computadora:", valor_total_computadora)


#Intento de calculo de envido 
igual_palo=0
if 'E' in cartas_computadora:
    igual_palo+=1
elif 'O' in cartas_computadora:
    igual_palo+=1
elif 'B' in cartas_computadora:
    igual_palo+=1
elif 'C' in cartas_computadora:
    igual_palo+=1
    
if igual_palo <2:
    igual=True
    
print (igual)
