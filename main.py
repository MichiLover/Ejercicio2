import csv
from ClaseViajero import Viajero 

if __name__== '__main__':

    #apartado 1
    print("EJERCICIO 1")
    print("\n")
    archivo = open("datos.csv")
    reader = csv.reader(archivo,delimiter=",")
    bandera = True

    for fila in reader:
        if bandera:
            bandera = False
        else:
            newViajero = Viajero()
            newViajero.crearViajero(fila[0],fila[1],fila[2],fila[3],fila[4])    
            print("\n")
    archivo.close()


    #apartado 2
    print("EJERCICIO 2")
    print("\n")
    archivo2 = open("datos.csv")
    reader = csv.reader(archivo2,delimiter=",")
    numero = input ("Ingresar un numero de viajero frecuente: ")
    bandera = True

    for fila in reader:
        if bandera:
            bandera = False
        else:
            newViajero2 = Viajero()
            respuesta = newViajero2.compara(fila[0],fila[1],fila[2],fila[3],int(fila[4]),numero)    
            print("\n")

            if not respuesta: 
                print("Numero de viajero correcto\n")
                menu = int (input("Elegir opción: \n 1- Consultar cantidad de millas \n 2- Acumular millas \n 3- Canjear millas\n"))

                while menu != 0:
                    if menu == 1:
                        print("Cantidad total de millas es: {}".format(newViajero2.cantidadTotaldeMillas()))
                    elif menu == 2:
                        millas = int(input("Ingresar la cantidad de millas recorridas: "))
                        total = newViajero2.acumularMillas(millas)
                        print("Total de millas acumuladas:",total)
                        print("\n")
                    elif menu == 3:
                        canje = int(input("Ingresar la cantidad de millas a canjear: "))
                        monto = newViajero2.canjearMillas(canje)
                        print("El total de millas acumuladas es: {}".format(monto))
                        print("\n")
                    else:
                        print("Elije otra opción, cero para finalizar\n")
                        print("\n")
                    menu = int (input("Elegir opción: \n 1- Consultar cantidad de millas \n 2- Acumular millas \n 3- Canjear millas\n"))



    archivo.close()
    