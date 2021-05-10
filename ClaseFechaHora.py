class FechaHora:                                      #ejercicio 6
    __year = 0
    __mes = 0
    __dia = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    __meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    def __init__(self,a=2020,mess=1,d=1,h=0,m=0,s=0):
        if (self.verificarHora(h,m,s))and(self.verificarFecha(a,mess,d)):
            self.__year=a
            self.__mes=mess
            self.__dia=d
            self.__hora=h
            self.__minutos=m
            self.__segundos=s
        else:
            print("ERROR, Los datos que ingreso son invalidos")
            self.__year = -1
    def test(self):
        datosCorrectos1= FechaHora(2020,5,17,20,50,58)       #Fecha y hora validas
        datosIncorrectos1= FechaHora(2017,13,18,5,13,51)   #Fecha y hora no validas, mes invalido
        datosCorrectos2= FechaHora(2016,2,29,1,4,0)       #Fecha y hora validos, año bisiesto
        datosIncorrectos2= FechaHora(2015,2,29,23,59,59)   #Fecha y hora invalidos, año no bisiesto con fecha no existente
        datosCorrectos1.Mostrar()
        input()
        datosIncorrectos1.Mostrar()
        input()
        datosCorrectos2.Mostrar()
        input()
        datosIncorrectos2.Mostrar()
        print("\nTEST REALIZADO EXITOSAMENTE\n")
    def Mostrar(self):
        if self.__year != -1:      #si la fecha es valida entonces se muestra, el atributo year tiene el valor -1 solo cuando los datos de ingreso no fueron validos
            print(str(self.__hora)+'/',str(self.__minutos)+'/',str(self.__segundos),'  ',str(self.__dia)+'/',str(self.__mes)+'/',str(self.__year))
        else:
            print("No es posible Mostrar por pantalla la Fecha y la Hora ya que los datos de ingreso son incorrectos")
    def verificarHora(self,h,m,s):
        if (h>=0)and(h<=23)and(m>=0)and(m<=59)and(s>=0)and(s<=59) :
            return True
        else:
            return False
    def verificarFecha(self,a,mess,d):
        if (a>0)and(mess>=1)and(mess<=12)and(d>=1)and(d<=31):
            if (mess==2)and(d==29)and(self.verificarBisiesto(a)):
                return True
            elif self.verificarMesDia(mess,d) == 0:
                return True
            else:
                return False
    def verificarBisiesto(self,a):
        if a % 4 !=0:
            return False
        elif (a % 4 == 0)and(a % 100 != 0):
            return True
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 != 0):
            return False
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 == 0):
            return True
    def verificarMesDia(self,mess,d):
        if ((mess==self.__meses[0])or(mess==self.__meses[2])or(mess==self.__meses[4])or(mess==self.__meses[6])or(mess==self.__meses[7])or(mess==self.__meses[9])or(mess==self.__meses[11]))and(d>31): #verifica que los meses que tienen 31 dias no se ingrese un dia mayor que 31
            return 1
        elif ((mess==self.__meses[3])or(mess==self.__meses[5])or(mess==self.__meses[8])or(mess==self.__meses[10]))and(d>30):  #verifica que en los meses que tienen 30 dias no se ingrese un dia mayor que 30
            return 2
        elif (mess==self.__meses[1])and(d>28):   #verifica que en el mes de febrero no se ingrese un dia mayor a 28
            return 3
        else:
            return 0              #si no es ninguna de las anteriores entonces la fecha es correcta
    def verificarMesDiaParaLista(self,listaFechaHora):
        if ((listaFechaHora[4]==1)or(listaFechaHora[4]==3)or(listaFechaHora[4]==5)or(listaFechaHora[4]==7)or(listaFechaHora[4]==8)or(listaFechaHora[4]==10)or(listaFechaHora[4]==12))and(listaFechaHora[3]>31):
            return 1
        elif ((listaFechaHora[4]==4)or(listaFechaHora[4]==6)or(listaFechaHora[4]==9)or(listaFechaHora[4]==11))and(listaFechaHora[3]>30):
            return 2
        elif (listaFechaHora[4]==2)and(listaFechaHora[3]>28):
            return 3
        else:
            return 0
    def PonerEnHora(self,h=0,m=0,s=0):
        if self.__year != -1:
            if self.verificarHora(h,m,s):
                self.__hora=h
                self.__minutos=m
                self.__segundos=s
            else:
                print("Datos de ingreso invalidos")
        else:
            print("No es posible PonerEnHora ya que los datos de ingreso fueron invalidos")
    def AdelantarHora(self,listaFechaHora):
            if (listaFechaHora[0] > 59)or(listaFechaHora[1] > 59)or(listaFechaHora[2] > 23):
                cont1=0
                cont2=0
                cont3=0
                while listaFechaHora[0] > 59:
                    cont1 += 1
                    listaFechaHora[0] -= 60
                listaFechaHora[1] += cont1
                while listaFechaHora[1] > 59:
                    cont2 += 1
                    listaFechaHora[1] -= 60
                listaFechaHora[2] += cont2
                while listaFechaHora[2] > 23:
                    cont3 += 1
                    listaFechaHora[2] -= 24
                listaFechaHora[3] += cont3
                self.AdelantarFecha(listaFechaHora)
    def AdelantarFecha(self,listaFechaHora):
        if listaFechaHora[4]>12:
            listaFechaHora[4] -= 12
            listaFechaHora[5] += 1
        bandera = True
        while bandera == True:
            if (self.verificarMesDiaParaLista(listaFechaHora) == 1):
                listaFechaHora[3] -= 31
                listaFechaHora[4] += 1
                if listaFechaHora[4] > 12:
                    listaFechaHora[4] -= 12
                    listaFechaHora[5] += 1
            elif (self.verificarMesDiaParaLista(listaFechaHora) == 2):
                listaFechaHora[3] -= 30
                listaFechaHora[4] += 1
            elif (self.verificarMesDiaParaLista(listaFechaHora) == 3):
                if self.verificarBisiesto(listaFechaHora[5]):
                    if listaFechaHora[3] > 29:
                        listaFechaHora[3] -= 29
                        listaFechaHora[4] += 1
                else:
                    listaFechaHora[3] -= 28
                    listaFechaHora[4] += 1
            else:
                bandera = False
    def RestarFecha(self,otraFechaHora1):
        contResta1= 0
        contResta2= 0
        contResta3= 0
        restaYear= self.__year - otraFechaHora1.getYear()
        if self.__segundos < otraFechaHora1.getSegundos():
            restaSegundos= 60 - (otraFechaHora1.getSegundos() - self.__segundos)
            contResta1 += 1
        else:
            restaSegundos= self.__segundos - otraFechaHora1.getSegundos()
        if self.__minutos < (otraFechaHora1.getMinutos() + contResta1):
            restaMinutos= 60 - ((otraFechaHora1.getMinutos() + contResta1) - self.__minutos)
            contResta2 += 1
        else:
            restaMinutos= self.__minutos - (otraFechaHora1.getMinutos() + contResta1)
        if self.__hora < (otraFechaHora1.getHora() + contResta2):
            restaHora= 24 - ((otraFechaHora1.getHora() + contResta2) - self.__hora)
            contResta3 += 1
        else:
            restaHora= self.__hora - (otraFechaHora1.getHora() + contResta2)
        if self.__mes < otraFechaHora1.getMes():
            restaMes= 12 - (otraFechaHora1.getMes() - self.__mes)
            restaYear -= 1
        else:
            restaMes= self.__mes - otraFechaHora1.getMes()
        if self.__dia < (otraFechaHora1.getDia() + contResta3):
            if ((restaMes - 1) == 1)or((restaMes - 1) == 3)or((restaMes - 1) == 5)or((restaMes - 1) == 7)or((restaMes - 1) == 8)or((restaMes - 1) == 10):
                restaDia= 31 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                restaMes -= 1
            elif ((restaMes - 1) == 4)or((restaMes - 1) == 6)or((restaMes - 1) == 9)or((restaMes - 1) == 11):
                restaDia= 30 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                restaMes -= 1
            elif ((restaMes - 1) == 2):
                if self.verificarBisiesto(restaYear):
                    restaDia= 29 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                    restaMes -= 1
                else:
                    restaDia= 28 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                    restaMes -= 1
            elif (restaMes == 1):                          #Si se encuentra en el mes de enero resta 1 mes y queda en diciembre del anterior año
                restaDia= 31 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                restaMes = 12
                restaYear -= 1
            elif (restaMes == 0):                          #Puede darse el caso que el mes resultante de restar los dos meses ingresados sea 0, en ese caso el mes 0 corresponde al mes 12
                restaDia= 30 - ((otraFechaHora1.getDia() + contResta3) - self.__dia)
                restaMes = 11
                restaYear -= 1
        else:
            restaDia= self.__dia - (otraFechaHora1.getDia() + contResta3)
        return restaSegundos + (restaMinutos * 60) + (restaHora * 3600) + (restaDia * 86400) + (restaMes * 2628000) + (restaYear * 31557600)
    def getSegundos(self):
        return self.__segundos
    def getMinutos(self):
        return self.__minutos
    def getHora(self):
        return self.__hora
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getYear(self):
        return self.__year
    def __add__(self,otraFechaHora):
        sumaYear= self.__year + otraFechaHora.getYear()
        sumaMes= self.__mes + otraFechaHora.getMes()
        sumaDia= self.__dia + otraFechaHora.getDia()
        sumaHora= self.__hora + otraFechaHora.getHora()
        sumaMinutos= self.__minutos + otraFechaHora.getMinutos()
        sumaSegundos= self.__segundos + otraFechaHora.getSegundos()
        listaFechaHora = [sumaSegundos,sumaMinutos,sumaHora,sumaDia,sumaMes,sumaYear]
        self.AdelantarHora(listaFechaHora)
        return FechaHora(listaFechaHora[5],listaFechaHora[4],listaFechaHora[3],listaFechaHora[2],listaFechaHora[1],listaFechaHora[0])
    def __sub__(self,otraFechaHora1):
        return self.RestarFecha(otraFechaHora1)
    def __gt__(self,otraFechaHora2):
        bandera = None
        if self.__year > otraFechaHora2.getYear():
            bandera = True
        elif self.__year < otraFechaHora2.getYear():
            bandera= False
        else:
            if self.__mes > otraFechaHora2.getMes():
                bandera= True
            elif self.__mes < otraFechaHora2.getMes():
                bandera= False
            else:
                if self.__dia > otraFechaHora2.getDia():
                    bandera= True
                elif self.__dia < otraFechaHora2.getDia():
                    bandera= False
                else:
                    if self.__hora > otraFechaHora2.getHora():
                        bandera= True
                    elif self.__hora < otraFechaHora2.getHora():
                        bandera= False
                    else:
                        if self.__minutos > otraFechaHora2.getMinutos():
                            bandera= True
                        elif self.__minutos < otraFechaHora2.getMinutos():
                            bandera= False
                        else:
                            if self.__segundos > otraFechaHora2.getSegundos():
                                bandera= True
                            elif self.__segundos < otraFechaHora2.getSegundos():
                                bandera= False
                            else:
                                bandera= False
        return bandera


