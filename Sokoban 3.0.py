# -*- coding: cp1252 -*-
import Movi #Importamos el movimiento que se definio como primer paso

print "'#' -> Pared, ' '-> Espacio, '$'->Caja, '.'->Meta "
print "'@' -> Jugador '*'->Caja en meta '&'->Mu�eco en meta"
print " a = Izquierda d = Derecha \n w = Arriba    s = Abajo \n"
print "Usa la letra (p) para activar Poder de bomba"


	
nivel = 0
while nivel < 5:
    nivel+=1 #Se usara un contador al pasar cada nivel
    
    with open("nivel"+str(nivel)+".lnpr", "r") as f: #Se abre un archivo en modo lectura y se le asigna a una variable
              Matriz = [linea.split(",") for linea in f] #Aqui se crea la Matriz

    print "Nivel", nivel
    cadena =((x,y)for y,  row in enumerate(Matriz)for x,  elemento in enumerate(row) if elemento == "@")
    
    for e in cadena:
        print "Posicion = ", e[0], e[1]
        
    posicionx = e[0]
    posiciony = e[1]
    
    Movi.Movimiento(Matriz = Matriz, posicionx = posicionx, posiciony = posiciony) #Llamamos la funcion Movimiento para poder jugar 

print "Juego terminado"

        

        

