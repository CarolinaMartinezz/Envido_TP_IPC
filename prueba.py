import random #Para poder luego utilizar la librería "random"


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
#Utilizamos un diccionario para asignar el valor de las cartas, con el sistema "clave", "valor"
#De esta forma, podemos acceder facilmente a esos valores, llamando simplemente a la clave que corresponda.


# Creamos las siguientes variables para darle inicio al cálculo de puntos totales. Al comienzo tanto la
# computadora como el usuario tienen 0 puntos. No obstante, como se verá luego, la intención es que luego
# se empiecen a acumular con los puntos que van obteniendo.
puntos_total_jugador=0
puntos_total_computadora=0


#Definición de quien es mano al comienzo del juego 
quien_mano=['mano_jugador', 'mano_comp']
es_mano= random.choice(quien_mano) # Utilizamos "random.choice" para seleccionar un elemento aleatorio 
                                   # de la lista de la variable "quien_mano". De esta forma, se define
                                   # al azar si quien comienza es la computadora o el usuario.


#Mensaje de bienvenida, el cual se verá solo al comienzo del juego
print (
    '''
     ╔═.♣.═════════════════════════════════╗
        Bienvenido al simulador del envido
     ╚═════════════════════════════════.♠.═╝
    '''
)

#Realizamos un while para preguntarle al usuario hasta cuantos puntos quiere jugar
i=0 
while i==0:
    puntos_fin_juego=input('¿Hasta cuantos puntos desea jugar?: ')
    if puntos_fin_juego.isnumeric():  #La función "is.numeric" la utilizamos para que reconozca
                                      #si el string introducido contiene solo números
        print(f'  ----- jugando hasta {puntos_fin_juego} puntos -----')
        print ('')
        i+=888 #PREGUNTAR MARCOS
    else:
        print('  ◈ error - ingrese un valor válido ◈  ')

puntos_fin_juego=int(puntos_fin_juego) # Utilizamos "int()" para convertirlo en entero y que
                                       # funcione como un número y no como un string
   

# El ciclo while a continuación es el principal. El mismo provoca que hayan rondas del juego  
# siempre y cuando el usuario y la computadora tengan una menor cantidad de puntos que las que el 
# usuario estableció como fin del juego en el input anterior.
while puntos_total_jugador <puntos_fin_juego and puntos_total_computadora <puntos_fin_juego:
   
   
    #REPARTIDOR DE CARTAS
    mazo_jugador= random.sample(mazo_cartas, 3) #El "random.sample" lo que hace es repartir cartas al jugador 
                                                #de manera aleatoria y asegurarse de que las cartas repartidas
                                                #no se repitan.
    for carta_usada in mazo_jugador:
        mazo_cartas.remove(carta_usada) # En cada iteración, elimina la carta (carta_usada) del mazo
                                        # principal "mazo_cartas". Esto garantiza que las cartas 
                                        # repartidas al jugador no estén disponibles en el mazo principal

    mazo_comp= random.sample (mazo_cartas, 3) # Realizo lo mismo que en el código anterior, pero en este caso con
                                              # las cartas de la computadora.
    for carta_usada in mazo_comp:
        mazo_cartas.remove(carta_usada)
   
    #Ahora, vuelvo a agregar las cartas eliminadas del mazo, ya que en las siguientes rondas esas cartas si
    #pueden aparecer (la idea es que solo en la misma ronda no estén repetidas)
    mazo_cartas.extend(mazo_jugador)
    mazo_cartas.extend(mazo_comp)
   
    #Creo la variable "paloX" para poder acceder solamente al palo de la carta
    #Accedo a los palos de las cartas del usuario:
    palo1=mazo_jugador[0][0] #
    palo2=mazo_jugador[1][0]
    palo3=mazo_jugador[2][0]

    #Accedo a los palos de las cartas de la computadora:
    palo1c=mazo_comp[0][0]
    palo2c=mazo_comp[1][0]
    palo3c=mazo_comp[2][0]


    #Creo la variable "valor_carta_X" para poder acceder a los valores de las cartas, los cuales se encuentran
    #dentro de un diccionario
    #Accedo a los valores de las cartas del usuario:
    valor_carta_1_jugador = valores_mazo_general[mazo_jugador[0]] # "valor_mazo_general" es el diccionario, mientras
                                                                  # que "mazo_jugador" hace referencia a la clave 
                                                                  # de la cartaque de manera aleatoria se le asignó.
                                                                  # El numero del corchete es porque quiero que 
                                                                  # seleccione la primer carta. 
    valor_carta_2_jugador = valores_mazo_general[mazo_jugador[1]]
    valor_carta_3_jugador = valores_mazo_general[mazo_jugador[2]]

    #Accedo a los valores de las cartas de la computadora:
    valor_carta_1_computadora = valores_mazo_general[mazo_comp[0]]
    valor_carta_2_computadora = valores_mazo_general[mazo_comp[1]]
    valor_carta_3_computadora = valores_mazo_general[mazo_comp[2]]


    #lista con valores
    lista_valor_jugador=[valor_carta_1_jugador, valor_carta_2_jugador, valor_carta_3_jugador]
    lista_valor_computadora=[valor_carta_1_computadora, valor_carta_2_computadora, valor_carta_3_computadora]
    #Esto me permite que los valores de las cartas se encuentren dentro de una lista, para luego aplicar
    #la función sorted y ordenarlas del menor al mayor valor.



    #Evaluo, de acuerdo a las cartas que tiene el usuario, cuantos puntos acumula en esta ronda.
    puntos_jugador=0
    if palo1==palo2==palo3:
        lista= sorted(lista_valor_jugador)
        puntos_jugador=lista[1]+lista[2]+20 #Lo que hacemos es que si el usuario tiene tres cartas iguales, que
                                            #tome los dos valores más grandes (por eso usammos sorted antes), los
                                            #sume y luego sume 20. 
    elif palo1==palo2 or palo1==palo3 or palo2==palo3:
        if palo1==palo2:
            puntos_jugador=valor_carta_1_jugador + valor_carta_2_jugador +20 
        elif palo1==palo3:
            puntos_jugador=valor_carta_1_jugador + valor_carta_3_jugador +20
        elif palo2==palo3:
            puntos_jugador=valor_carta_2_jugador + valor_carta_3_jugador +20
    #En estos tres casos en los que hay dos cartas del mismo palo, los suma y suma 20.
    else:
        puntos_jugador=max(lista_valor_jugador) #Si no tiene cartas del mismo palo, toma el valor máximo
   


    #Al igual que en las lineas anteriores, evaluo, de acuerdo a las cartas que tiene la computadora cuantos 
    #puntos acumula en esta ronda.
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
   
   
    #Presentación de cuales son las cartas que tiene el jugador y cual es su envido (se repite en cada ronda)
   
    print (f'Sus cartas son: {mazo_jugador}')
    print(f'Tenés un envido de: {puntos_jugador}')
    print ('')
    
    #El siguiente código es para que, tal y como se juega en la vida real, el que empiece siendo mano no lo sea
    #en la ronda siguiente, sino que empieza y es mano el otro jugador.
    if es_mano == 'mano_jugador':
        es_mano= 'mano_comp'
    elif es_mano=='mano_comp':
        es_mano='mano_jugador'
   
   
   #Ahora sí, comienza el código del juego:
   
   #En el caso de que el usuario comience siendo mano:
   
    if es_mano=='mano_jugador': 
        print('Usted es mano')
        eleccion=str.lower(input('¿Que queres jugar? ¿envido o no envido?: '))
        #Utilizamos "str.lower" para convertir el texto ingresado por el usuario en minúsculas y que no haya 
        #problema si ingresa el texto en mayúscula
        
        #Primero evaluamos las posibilidades cuando el usuario quiere envido:
        
        if eleccion=='envido':
        #La computadora, de acuerdo a cuanto envido tenga, responde con quiero, no quiero o envido:
            if puntos_computadora < 20:
                print ('computadora: no quiero')
                puntos_total_jugador +=1 #Como la computadora no quiso envido, el usuario en esta ronda acumula 1 punto
                print('')
                print (f'mazo computadora: {mazo_comp}')
                print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                print ('Sumaste 1 punto!')
           
            elif puntos_computadora >=20:
                print ('computadora: envido')
                #En este caso, como hay un envido-envido, se comparan los envidos del usuario y de la computadora
                eleccion = input("¿quiero o no quiero?: ")
                if eleccion == "quiero":
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
            
                        
                elif eleccion == "no quiero":
                    puntos_total_computadora += 2
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                    print ('Gana la computadora :( , suma 2 puntos.')
                    
                else:
                    print("'  ◈ error - ingrese un valor válido ◈  '")
                    
            else:
                print ('computadora: quiero')
                #Como la computadora quiere envido, se copara su envido con el del usuario
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
                           
        #Ahora evaluamos las posibilidades cuando el usuario no quiere envido:      
        
        elif eleccion== 'no envido':
        #Al igual que anteriormente, la computadora, de acuerdo a cuanto envido tenga, responde con quiero, no quiero o envido:
            if puntos_computadora <20:
                print ('computadora: no canta envido')
                print ('Nadie cantó envido') #Como ninguno quiso envido, no se suman puntos
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
                            
                   
    #Por otro lado, en el caso de que la computadora comience siendo mano:
    #Primero determino que es lo que va a querer la computadora.
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
               
        #Evaluo las posibilidades cuando la computadora quiere envido:
         
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
                if puntos_computadora >= 20:
                    print("computadora: quiero")
                    
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
                    
                    elif puntos_computadora == puntos_jugador:
                        if es_mano == "mano_jugador":
                            puntos_total_jugador += 4
                        else:
                            puntos_total_computadora +=4
                
                
                elif puntos_computadora < 20:
                    print("computadora: no quiero")
                    puntos_total_jugador +=2
                    print('')
                    print (f'mazo computadora: {mazo_comp}')
                    print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
                    print ('Sumaste 2 puntos!')
                 
            else:
                print('  ◈ error - ingrese un valor válido ◈  ')
               
        #Evaluo las posibilidades cuando la computadora no quiere envido:
        
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
                print ('Nadie cantó envido')
                print('')
                print (f'mazo computadora: {mazo_comp}')
                print (f'Usted tiene un envido de {puntos_jugador} y la computadora de {puntos_computadora}')
            else:
                print('  ◈ error - ingrese un valor válido ◈  ')
        else:
            print('  ◈ error - ingrese un valor válido ◈  ')
           
               
   
         
         
    # Los siguientes prints son para que se anuncie el contador de puntos en cada ronda, especificando cuantos
    # puntos tiene el usuario y cuantos la computadora
    print('--------------------------------------')
    print(f'La computadora tiene {puntos_total_computadora} punto/s.')
    print(f'Usted tiene {puntos_total_jugador} punto/s.')
    print('--------------------------------------')
   

    #El siguiente if detecta si se tiene que pasar de ronda o avisar que terminó el juego. 
    if puntos_total_computadora >= puntos_fin_juego: #Si los puntos de la computadora son mayores a los puntos que
                                                     #el usuario asigno como fin del juego, se ejecutan los prints
        print(f"La computadora llegó a los {puntos_fin_juego} puntos, ganó")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
        
    elif puntos_total_jugador >= puntos_fin_juego: # Si los puntos del usuario son mayores a los puntos que
                                                   # asignó previamnete como fin del juego, se ejecutan los prints
        print(f"Llegaste a los {puntos_fin_juego} puntos, ganaste!")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
        
    elif puntos_computadora == puntos_fin_juego and puntos_total_jugador == puntos_fin_juego: #Si el usuario y la computadora
                                                                                              #tienen los mismos puntos,
                                                                                              #es un empate
        print(f"Tanto vos como la computadora llegaron a los {puntos_fin_juego} puntos. Empate")
        print("======================================")
        print ('         ༺★ 𝓕𝓘𝓝  𝓓𝓔𝓛 𝓙𝓤𝓔𝓖𝓞 ★༻')
        print("======================================")
        
    else: #Este else implica que, todavía ni el jugador ni la computadora llegaron a los puntos del fin del juego,
          # por lo que se pasa a la siguiente ronda
        print("╔═════════════════════════════════════╗")
        print ('         ༺★ Siguiente ronda ★༻')
        print("╚═════════════════════════════════════╝")







