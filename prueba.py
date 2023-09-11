import random


# MAZO DE LAS CARTAS
mazo_cartas = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E10", "E11", "E12",
                "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B10", "B11", "B12",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C10", "C11", "C12",
                "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O10", "O11", "O12"]
# E = espada
# B = basto
# C = copa
# O = oro

valores_mazo_general = {
    "E1": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6, "E7": 7, "E10": 0, "E11": 0, "E12": 0,
    "B1": 1, "B2": 2, "B3": 3, "B4": 4, "B5": 5, "B6": 6, "B7": 7, "B10": 0, "B11": 0, "B12": 0,
    "C1": 1, "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C10": 0, "C11": 0, "C12": 0,
    "O1": 1, "O2": 2, "O3": 3, "O4": 4, "O5": 5, "O6": 6, "O7": 7, "O10": 0, "O11": 0, "O12": 0
}


#inicio de variable para calculo de puntos totales
puntos_total_jugador=0
puntos_total_computadora=0


#Decide quien empieza la ronda
quien_mano=['mano_jugador', 'mano_comp']
es_mano= random.choice(quien_mano)


#bienvenida
print (
    '''
     ╔═.♣.═══════════════════════════════╗
       𝓑𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 𝓪𝓵 𝓼𝓲𝓶𝓾𝓵𝓪𝓭𝓸𝓻 𝓭𝓮 𝓮𝓷𝓿𝓲𝓭𝓸
     ╚═══════════════════════════════.♠.═╝
    '''
)

#no se
puntos_fin_juego=int(input('¿Hasta cuantos puntos desea jugar?: '))
print(f'  ----- jugando hasta {puntos_fin_juego} puntos -----')
print ('')


   
#While de las rondas de la jugada, el cual seguirá funcionando hasta que el jugador o la computadora lleguen a 15 puntos  
while puntos_total_jugador <puntos_fin_juego and puntos_total_computadora <puntos_fin_juego:
   
   
    #REPARTIDOR DE CARTAS
    #manos = random.sample(mazo_cartas , 6)
    mazo_jugador= random.sample(mazo_cartas, 3) #creo el mazo del jugador y elimino las cartas del mazo principal
    for carta_usada in mazo_jugador:
        mazo_cartas.remove(carta_usada)


    mazo_comp= random.sample (mazo_cartas, 3) #creo el mazo de la computadora y elimino las cartas del mazo principal
    for carta_usada in mazo_comp:
        mazo_cartas.remove(carta_usada)
   
    #Vuelvo a agregar las cartas eliminadas del mazo
    mazo_cartas.extend(mazo_jugador)
    mazo_cartas.extend(mazo_comp)
   
    #ACCESO AL PALO DE LA CARTA
    palo1=mazo_jugador[0][0]
    palo2=mazo_jugador[1][0]
    palo3=mazo_jugador[2][0]


    palo1c=mazo_comp[0][0]
    palo2c=mazo_comp[1][0]
    palo3c=mazo_comp[2][0]




    #ACCESO AL VALOR DE LAS CARTAS
    valor_carta_1_jugador=valores_mazo_general[mazo_jugador[0]]
    valor_carta_2_jugador = valores_mazo_general[mazo_jugador[1]]
    valor_carta_3_jugador = valores_mazo_general[mazo_jugador[2]]


    valor_carta_1_computadora = valores_mazo_general[mazo_comp[0]]
    valor_carta_2_computadora = valores_mazo_general[mazo_comp[1]]
    valor_carta_3_computadora = valores_mazo_general[mazo_comp[2]]


    #lista con valores
    lista_valor_jugador=[valor_carta_1_jugador, valor_carta_2_jugador, valor_carta_3_jugador]
    lista_valor_computadora=[valor_carta_1_computadora, valor_carta_2_computadora, valor_carta_3_computadora]




    #mazo_jugador
    puntos_jugador=0
    if palo1==palo2==palo3:
        lista= sorted(lista_valor_jugador)
        puntos_jugador=lista[1]+lista[2]+20
    elif palo1==palo2 or palo1==palo3 or palo2==palo3:
        if palo1==palo2:
            puntos_jugador=valor_carta_1_jugador + valor_carta_2_jugador +20
        elif palo1==palo3:
            puntos_jugador=valor_carta_1_jugador + valor_carta_3_jugador +20
        elif palo2==palo3:
            puntos_jugador=valor_carta_2_jugador + valor_carta_3_jugador +20
    else:
        puntos_jugador=max(lista_valor_jugador)
   


    #mazo computadora
    puntos_computadora=0
    if palo1c==palo2c==palo3c:
        lista= sorted(lista_valor_computadora)
        puntos_computadora=lista[1]+lista[2]+20
    elif palo1c==palo2c or palo1c==palo3c or palo2c==palo3c:
        if palo1c==palo2c:
            puntos_computadora=valor_carta_1_computadora + valor_carta_2_computadora +20
        elif palo1c==palo3c:
            puntos_computadora=valor_carta_1_computadora + valor_carta_3_computadora +20
        elif palo2c==palo3c:
            puntos_computadora=valor_carta_2_computadora + valor_carta_3_computadora +20
    else:
        puntos_computadora=max(lista_valor_computadora)    
   
   
    #presentación
   
    print (f'Sus cartas son: {mazo_jugador}')
    print(f'Tenés un envido de: {puntos_jugador}')
    print ('')
    
    #cambiar mano
    if es_mano == 'mano_jugador':
        es_mano= 'mano_comp'
    elif es_mano=='mano_comp':
        es_mano='mano_jugador'
   
   
   #empieza el juego:
   
    if es_mano=='mano_jugador':
        print('Usted es mano')
        eleccion=str.lower(input('¿Que queres jugar? ¿envido o no envido?: '))
        if eleccion=='envido':
            if puntos_computadora <20:
                print ('computadora: no quiero')
                puntos_total_jugador +=1
                print('')
                print (f'mazo computadora: {mazo_comp}')
                print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                print ('Sumaste 1 punto!')
           
            elif puntos_computadora >=20:
                print ('computadora: envido')
                if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 4 puntos!')
                elif puntos_computadora>puntos_jugador:
                    puntos_total_computadora+=4
                    print('')
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                    print ('Gana la computadora :( , suma 4 puntos.')
           
            else:
                print ('computadora: quiero')
                if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 4 puntos!')
                   
                elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 4 puntos.')
                           
               
        elif eleccion== 'no envido':
            if puntos_computadora <20:
                print ('computadora: no canta envido')
                print ('Empate')
                print('')
                print (f'mazo computadora: {mazo_comp}')
                print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
           
            elif puntos_computadora >=20:
                print ('computadora: envido')
                eleccion_segunda=input('envido, no quiero: ')
                if eleccion_segunda== 'envido':
                    if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=4 #preguntar cuanto suma
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 4 puntos!')
                   
                    elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=4 #preguntar cuanto suma
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 4 puntos')
                   
                elif eleccion_segunda== 'no quiero':
                    puntos_total_computadora+=1
                    print('')
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                    print ('Gana la computadora :( , suma 1 punto')
                else:
                    print('  ◈ error - ingrese un valor válido ◈  ')
        else:
            print('  ◈ error - ingrese un valor válido ◈  ')
                            
                   
                   
    elif es_mano=='mano_comp':
        print('La computadora es mano')
        if puntos_computadora <20:
            posibilidades=['no envido','no envido', 'envido'] #más probable que salga 'no envido' (66%)
            eleccion=random.choice(posibilidades)
            if eleccion=='envido':
                print ('computadora: envido')
            elif eleccion=='no envido':
                print ('computadora: no envido')
        elif puntos_computadora >=20:
            eleccion='envido'
            print ('computadora: envido')
               
               
        if eleccion=='envido':
            eleccion= str.lower(input('¿Que queres jugar? ¿quiero, no quiero o envido?: '))
            if eleccion == 'quiero':
                if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=2
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 2 puntos!')
                   
                elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=2
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 2 puntos')
                   
            elif eleccion=='no quiero':
                puntos_total_computadora+=1
                print ('gana la computadora :(')
            elif eleccion=='envido':
                if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 4 puntos!')
                   
                elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 4 puntos')
                   
                else:
                    print ('Empate')
                    print('')
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
            else:
                print('  ◈ error - ingrese un valor válido ◈  ')
               
           
        elif eleccion=='no envido':
            eleccion_humano=input('envido o no envido: ')
            if eleccion_humano=='envido':        
                if puntos_computadora <20:
                    eleccion='no envido'
                    print ('computadora: no envido')
                    puntos_total_jugador+=1
                    print('')
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                    print ('Sumaste 1 punto!')
               
                elif puntos_computadora >=28:
                    eleccion='envido'
                    print ('computadora: envido')
                    if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 4 puntos!')
                   
                    elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=4
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 4 puntos')
                   
                else:
                    print ('computadora: quiero')
                    if puntos_jugador>puntos_computadora:
                        puntos_total_jugador+=2
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Sumaste 2 puntos!')
                   
                    elif puntos_computadora>puntos_jugador:
                        puntos_total_computadora+=2
                        print('')
                        print (f'mazo computadora: {mazo_comp}')
                        print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                        print ('Gana la computadora :( , suma 2 puntos')
                   
                       
            elif eleccion_humano=='no envido':
                print ('Empate')
                print('')
                print (f'mazo computadora: {mazo_comp}')
                print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
            else:
                print('  ◈ error - ingrese un valor válido ◈  ')
        else:
            print('  ◈ error - ingrese un valor válido ◈  ')
           
               
   
         
         
    #Anuncia el contador de puntos en cada ronda               
    print('--------------------------------------')
    print(f'La computadora tiene {puntos_total_computadora} punto/s.')
    print(f'Usted tiene {puntos_total_jugador} punto/s.')
    print('--------------------------------------')
   

    #Detecta si se tiene que pasar de ronda o avisar que terminó el juego
    if puntos_total_computadora >= puntos_fin_juego:
        print(f"La computadora llegó a los {puntos_fin_juego} puntos, ganó")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
    elif puntos_total_jugador >= puntos_fin_juego:
        print(f"Llegaste a los {puntos_fin_juego} puntos, ganaste!")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
    elif puntos_computadora == puntos_fin_juego and puntos_total_jugador == puntos_fin_juego:
        print(f"Tanto vos como la computadora llegaron a los {puntos_fin_juego} puntos. Empate")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
    else:
        print("╔═════════════════════════════════════╗")
        print ('         ༺★ Siguiente ronda ★༻')
        print("╚═════════════════════════════════════╝")






   
#agregar función que reconozca cuando alguien gana
#explicar lo de volver a agregar cartas al mazo

