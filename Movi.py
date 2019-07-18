# -*- coding: cp1252 -*-
def Movimiento(Matriz, posicionx, posiciony):
    pasos = 0
    while True: #Inicia el ciclo
        pasos+=1
        for matrizx in Matriz:
            for matrizy in matrizx:
                print matrizy,
            print
            
        Mov = raw_input("�Hacia donde te quieres mover? \n ") #Pregunta hacia donde se desea mover el usuario
        #MOVIMIENTO A LA DERECHA

        cadena =((posicionx,posiciony)for posiciony,  row in enumerate(Matriz)for posicionx,  elemento in enumerate(row) if elemento == "@")
        for e in cadena:
            print "Posicion = ", e
            
        ele =((cajax,cajay)for cajay,  row in enumerate(Matriz) for cajax,  elemento in enumerate(row) if elemento == "$")

        suma = 0            
        for meta in ele:
            suma+=1
            
        if suma <= 0 or Mov == "b":
                if suma <= 0:
                    print "Nivel completado"
                    break
                elif Mov == "b":
                    print "Nivel cancelado"
                    break
        if Mov == "d":
            #Movimiento a la derecha si hay camino "044"
            if Matriz[posicionx][posiciony + 1] == " " and Matriz[posicionx][posiciony] == "@": 
                Matriz[posicionx][posiciony] = " "
                posiciony+= 1
                Matriz[posicionx][posiciony] = "@"
            
            elif Matriz[posicionx][posiciony + 1] == "$" and Matriz[posicionx][posiciony] == "@":
                #Movimiento a la derecha si hay caja y camino "014"
                if Matriz[posicionx][posiciony + 2] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posiciony+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony + 1] = "$"
                #Movimiento a la derecha si hay caja y meta "012"
                elif Matriz[posicionx][posiciony + 2] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posiciony+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony + 1] = "*"
                    
            #Si la posicion es igual a 6 y adelante hay una caja en meta
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony + 1] == "*":
                #mu�eco en meta, caja en meta y meta "652"
                if Matriz[posicionx][posiciony + 2] == ".":
                    Matriz[posicionx][posiciony] = "."
                    posiciony+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony + 1] = "*"
                #mu�eco en meta, caja en meta y camino "654"
                elif Matriz[posicionx][posiciony + 2] == " ":
                    Matriz[posicionx][posiciony] = "."
                    posiciony+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony + 1] = "$"
                
            #Movimiento a la derecha si hay caja en meta y camino
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx][posiciony + 1] == "*": 
                #054
                if Matriz[posicionx][posiciony + 2] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posiciony+= 1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony + 1] = "$"
                #052
                elif Matriz[posicionx][posiciony + 2] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posiciony+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony + 1] = "*"
                    
            #Metas y mu�eco consecutivo "622"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony + 1] == ".":
                Matriz[posicionx][posiciony] = "."
                posiciony+= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento a la derecha si el mu�eco esta sobre la meta "024"
            elif Matriz[posicionx][posiciony + 1] == "." and Matriz[posicionx][posiciony + 2] == " ": 
                Matriz[posicionx][posiciony] = " "
                posiciony+= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento a la derecha si hay mu�eco en meta y adelante un camino "644"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony + 1] == " ":
                Matriz[posicionx][posiciony] = "."
                posiciony+= 1
                Matriz[posicionx][posiciony] = "@"
                
            #Mu�eco en camino y si adelante hay meyta "402"
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx][posiciony + 1] == ".": 
                Matriz[posicionx][posiciony] = " "
                posiciony+=1
                Matriz[posicionx][posiciony] = "&"
                
            #Mu�eco en meta, adelante hay caja y adelante de la caja hay una meta o camino
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony + 1] == "$":
                if Matriz[posicionx][posiciony + 2] == ".": #612
                    Matriz[posicionx][posiciony] = "."
                    posiciony+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony + 1] = "*"
                elif Matriz[posicionx][posiciony + 2] == " ":#614
                    Matriz[posicionx][posiciony] = "."
                    posiciony+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony + 1] = "$"

        #MOVIMIENTO A LA IZQUIERDA
        elif Mov == "a":
            #Movimiento a la izquierda si hay camino "044"
            if Matriz[posicionx][posiciony - 1] == " " and Matriz[posicionx][posiciony] == "@": 
                Matriz[posicionx][posiciony] = " "
                posiciony-= 1
                Matriz[posicionx][posiciony] = "@"
            
            elif Matriz[posicionx][posiciony - 1] == "$" and Matriz[posicionx][posiciony] == "@":
                #Movimiento a la izquierda si hay caja y camino "014"
                if Matriz[posicionx][posiciony - 2] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posiciony-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony - 1] = "$"
                #Movimiento a la izquierda si hay caja y meta "012"
                elif Matriz[posicionx][posiciony - 2] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posiciony-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony - 1] = "*"
                    
            #Si la posicion es igual a 6 y adelante hay una caja en meta
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony - 1] == "*":
                #mu�eco en meta, caja en meta y meta "652"
                if Matriz[posicionx][posiciony - 2] == ".":
                    Matriz[posicionx][posiciony] = "."
                    posiciony-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony - 1] = "*"
                #mu�eco en meta, caja en meta y camino "654"
                elif Matriz[posicionx][posiciony - 2] == " ":
                    Matriz[posicionx][posiciony] = "."
                    posiciony-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony - 1] = "$"
                
            #Movimiento a la derecha si hay caja en meta y camino
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx][posiciony - 1] == "*": 
                #054
                if Matriz[posicionx][posiciony - 2] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posiciony-= 1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony - 1] = "$"
                #052
                elif Matriz[posicionx][posiciony - 2] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posiciony-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx][posiciony - 1] = "*"
                    
            #Metas y mu�eco consecutivo "622"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony - 1] == ".":
                Matriz[posicionx][posiciony] = "."
                posiciony-= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento a la derecha si el mu�eco esta sobre la meta "024"
            elif Matriz[posicionx][posiciony - 1] == "." and Matriz[posicionx][posiciony - 2] == " ": 
                Matriz[posicionx][posiciony] = " "
                posiciony-= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento a la derecha si hay mu�eco en meta y adelante un camino "644"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony - 1] == " ":
                Matriz[posicionx][posiciony] = "."
                posiciony-= 1
                Matriz[posicionx][posiciony] = "@"
                
            #Mu�eco en camino y si adelante hay meta "402"
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx][posiciony - 1] == ".": 
                Matriz[posicionx][posiciony] = " "
                posiciony-=1
                Matriz[posicionx][posiciony] = "&"
                
            #Mu�eco en meta, adelante hay caja y adelante de la caja hay una meta o camino
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx][posiciony - 1] == "$":
                if Matriz[posicionx][posiciony - 2] == ".": #612
                    Matriz[posicionx][posiciony] = "."
                    posiciony-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony - 1] = "*"
                elif Matriz[posicionx][posiciony - 2] == " ":#614
                    Matriz[posicionx][posiciony] = "."
                    posiciony-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx][posiciony - 1] = "$"
                    
        #MOVIMIENTO HACIA ARRIBA
        elif Mov == "w":
            #Movimiento hacia arriba si hay camino "044"
            if Matriz[posicionx - 1][posiciony] == " " and Matriz[posicionx][posiciony] == "@": 
                Matriz[posicionx][posiciony] = " "
                posicionx-= 1
                Matriz[posicionx][posiciony] = "@"
            
            elif Matriz[posicionx - 1][posiciony] == "$" and Matriz[posicionx][posiciony] == "@":
                #Movimiento arriba si hay caja y camino "014"
                if Matriz[posicionx - 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posicionx-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx - 1][posiciony] = "$"
                #Movimiento hacia arriba si hay caja y meta "012"
                elif Matriz[posicionx - 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posicionx-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx - 1][posiciony] = "*"
                    
            #Si la posicion es igual a 6 y adelante hay una caja en meta
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx - 1][posiciony] == "*":
                #mu�eco en meta, caja en meta y meta "652"
                if Matriz[posicionx - 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = "."
                    posicionx-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx - 1][posiciony] = "*"
                #mu�eco en meta, caja en meta y camino "654"
                elif Matriz[posicionx - 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = "."
                    posicionx-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx - 1][posiciony] = "$"
                
            #Movimiento hacia arriba si hay caja en meta y camino
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx - 1][posiciony] == "*": 
                #054
                if Matriz[posicionx - 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posicionx-= 1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx - 1][posiciony] = "$"
                #052
                elif Matriz[posicionx - 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posicionx-=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx - 1][posiciony] = "*"
                    
            #Metas y mu�eco consecutivo "622"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx - 1][posiciony] == ".":
                Matriz[posicionx][posiciony] = "."
                posicionx-= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento hacia arriba si el mu�eco esta sobre la meta "024"
            elif Matriz[posicionx - 1][posiciony] == "." and Matriz[posicionx - 2][posiciony] == " ": 
                Matriz[posicionx][posiciony] = " "
                posicionx-= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento hacia arriba si hay mu�eco en meta y adelante un camino "644"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx - 1][posiciony] == " ":
                Matriz[posicionx][posiciony] = "."
                posicionx-= 1
                Matriz[posicionx][posiciony] = "@"
                
            #Mu�eco en camino y si adelante hay meta "402"
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx - 1][posiciony] == ".": 
                Matriz[posicionx][posiciony] = " "
                posicionx-=1
                Matriz[posicionx][posiciony] = "&"
                
            #Mu�eco en meta, adelante hay caja y adelante de la caja hay una meta o camino
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx - 1][posiciony] == "$":
                if Matriz[posicionx - 2][posiciony] == ".": #612
                    Matriz[posicionx][posiciony] = "."
                    posicionx-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx - 1][posiciony] = "*"
                elif Matriz[posicionx - 2][posiciony] == " ":#614
                    Matriz[posicionx][posiciony] = "."
                    posicionx-= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx - 1][posiciony] = "$"

        #MOVIMIENTO HACIA ABAJO
        elif Mov == "s":
            #Movimiento abajo si hay camino "044"
            if Matriz[posicionx + 1][posiciony] == " " and Matriz[posicionx][posiciony] == "@": 
                Matriz[posicionx][posiciony] = " "
                posicionx+= 1
                Matriz[posicionx][posiciony] = "@"
            
            elif Matriz[posicionx + 1][posiciony] == "$" and Matriz[posicionx][posiciony] == "@":
                #Movimiento hacia abajo si hay caja y camino "014"
                if Matriz[posicionx + 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posicionx+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx + 1][posiciony] = "$"
                #Movimiento hacia abajo si hay caja y meta "012"
                elif Matriz[posicionx + 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posicionx+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx + 1][posiciony] = "*"
                    
            #Si la posicion es igual a 6 y adelante hay una caja en meta
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx + 1][posiciony] == "*":
                #mu�eco en meta, caja en meta y meta "652"
                if Matriz[posicionx + 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = "."
                    posicionx+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx + 1][posiciony] = "*"
                #mu�eco en meta, caja en meta y camino "654"
                elif Matriz[posicionx + 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = "."
                    posicionx+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx + 1][posiciony] = "$"
                
            #Movimiento hacia abajo si hay caja en meta y camino
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx + 1][posiciony] == "*": 
                #054
                if Matriz[posicionx + 2][posiciony] == " ":
                    Matriz[posicionx][posiciony] = " "
                    posicionx+= 1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx + 1][posiciony] = "$"
                #052
                elif Matriz[posicionx + 2][posiciony] == ".":
                    Matriz[posicionx][posiciony] = " "
                    posicionx+=1
                    Matriz[posicionx][posiciony] = "&"
                    Matriz[posicionx + 1][posiciony] = "*"
                    
            #Metas y mu�eco consecutivo "622"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx + 1][posiciony] == ".":
                Matriz[posicionx][posiciony] = "."
                posicionx+= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento hacia abajo si el mu�eco esta sobre la meta "024"
            elif Matriz[posicionx + 1][posiciony] == "." and Matriz[posicionx + 2][posiciony] == " ":
                Matriz[posicionx][posiciony] = " "
                posicionx+= 1
                Matriz[posicionx][posiciony] = "&"
                
            #Movimiento hacia abajo si hay mu�eco en meta y adelante un camino "644"
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx + 1][posiciony] == " ":
                Matriz[posicionx][posiciony] = "."
                posicionx+= 1
                Matriz[posicionx][posiciony] = "@"
                
            #Mu�eco en camino y si adelante hay meyta "402"
            elif Matriz[posicionx][posiciony] == "@" and Matriz[posicionx + 1][posiciony] == ".": 
                Matriz[posicionx][posiciony] = " "
                posicionx+=1
                Matriz[posicionx][posiciony] = "&"
                
            #Mu�eco en meta, adelante hay caja y adelante de la caja hay una meta o camino
            elif Matriz[posicionx][posiciony] == "&" and Matriz[posicionx + 1][posiciony] == "$":
                if Matriz[posicionx + 2][posiciony] == ".": #612
                    Matriz[posicionx][posiciony] = "."
                    posicionx+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx + 1][posiciony] = "*"
                elif Matriz[posicionx + 2][posiciony] == " ":#614
                    Matriz[posicionx][posiciony] = "."
                    posicionx+= 1
                    Matriz[posicionx][posiciony] = "@"
                    Matriz[posicionx + 1][posiciony] = "$"
                    
        elif Mov == "p":
            while True:
                for a in Matriz:
                    for b in a:
                        print b,
                    print
                Mov2 = raw_input("�Hacia donde te quieres mover? Tu XD \n ")
                if Mov2 == "w":
                    Matriz[posicionx][posiciony] = " "
                    posicionx = posicionx - 1
                    Matriz[posicionx][posiciony] = "@"
                elif Mov2 == "s":
                    Matriz[posicionx][posiciony] = " "
                    posicionx = posicionx + 1
                    Matriz[posicionx][posiciony] = "@"
                elif Mov2 == "a":
                    Matriz[posicionx][posiciony] = " "
                    posiciony = posiciony - 1
                    Matriz[posicionx][posiciony] = "@"
                elif Mov2 == "d":
                    Matriz[posicionx][posiciony] = " "
                    posiciony = posiciony + 1
                    Matriz[posicionx][posiciony] = "@"

                elif Mov2 == "p":
                        break
        else:
            print "Movimiento erroneo, por favor eliga una funcion correcta"
            
    for matrizx in Matriz:
        for matrizy in matrizx:
            print matrizy,
        print
    print "\n__________________________________________________________ \n"
