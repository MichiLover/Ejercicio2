class Viajero():
    __numV = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasAcum = ''

    #constructor
    def __init__(self):
        self.__numV = ''
        self.__dni = ''
        self.__nombre = ''
        self.__apellido = ''
        self.__millasAcum = ''

    #metodo crear viajero
    def crearViajero(self,num,dni,nom,ap,millas):

        self.__numV = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAcum = int(millas)

        print("Numero de viajero: {}".format(self.__numV))
        print("DNI del viajero: {}".format(self.__dni))
        print("Nombre del viajero: {}".format(self.__nombre))
        print("Apellido del viajero: {}".format(self.__apellido))
        print("Millas acumuladas: ",self.__millasAcum)
       
    #metodo apartado b
    def cantidadTotaldeMillas(self):

        return self.__millasAcum
    
    #metodo apartado c
    def acumularMillas(self,totalMillas):
        total = int(self.__millasAcum + totalMillas)
        return total

    #metodo apartado d
    def canjearMillas(self,canje):

        if canje <= self.__millasAcum:
            print("Se pueden canjear los puntos")
        else:
            print("ERROR-No se pueden canjear los puntos")

        monto = self.__millasAcum
        return monto


    #comparar numero de viajero

    def compara(self,num,dni,nom,ap,millas,xnumero):

        self.__numV = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAcum = millas

        for i in range(4):
            if xnumero == self.__numV:
                resp = False

            else:
                
                resp = True
        
        return resp

        