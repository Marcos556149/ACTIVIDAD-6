from ClaseFechaHora import FechaHora
if __name__=='__main__':
    pruebaTest= FechaHora()
    pruebaTest.test()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Sumar dos fechas")
        print("[2]...Restar dos fechas")
        print("[3]...Comparar entre dos fechas cual es mayor")
        print("[0]...Salir")
        try:
            op=int(input('Seleccione una opcion: '))
            if op in range(4):
                if op == 1:
                    print("INGRESE DATOS DE LA PRIMER FECHA A SUMAR\n")
                    year1=int(input('Ingrese año: '))
                    mes1=int(input('Ingrese mes: '))
                    dia1=int(input('Ingrese dia: '))
                    hora1=int(input('Ingrese hora: '))
                    minutos1=int(input('Ingrese minutos: '))
                    segundos1=int(input('Ingrese segundos: '))
                    a= FechaHora(year1,mes1,dia1,hora1,minutos1,segundos1)
                    if a.getYear() != -1:
                        print("\nINGRESE DATOS DE LA SEGUNDA FECHA A SUMAR\n")
                        year2= int(input('Ingrese año: '))
                        mes2= int(input('Ingrese mes: '))
                        dia2= int(input('Ingrese dia: '))
                        hora2= int(input('Ingrese hora: '))
                        minutos2= int(input('Ingrese minutos: '))
                        segundos2= int(input('Ingrese segundos: '))
                        b= FechaHora(year2,mes2,dia2,hora2,minutos2,segundos2)
                        if b.getYear() !=-1:
                            NuevaFecha = a+b
                            NuevaFecha.Mostrar()
                        else:
                            print("La segunda fecha ingresada es incorrecta por lo tanto no es posible realizar la suma")
                    else:
                        print("No es posible sumar otra fecha ya que la primer fecha ingresada es incorrecta")
                if op == 2:
                    print("\nINGRESE DATOS DE LA PRIMER FECHA A RESTAR\n")
                    year3= int(input('Ingrese año: '))
                    mes3= int(input('Ingrese mes: '))
                    dia3= int(input('Ingrese dia: '))
                    hora3= int(input('Ingrese hora: '))
                    minutos3= int(input('Ingrese minutos: '))
                    segundos3= int(input('Ingrese segundos: '))
                    c= FechaHora(year3,mes3,dia3,hora3,minutos3,segundos3)
                    if c.getYear() != -1:
                        print("\nINGRESE DATOS DE LA SEGUNDA FECHA A RESTAR\n")
                        year4= int(input("Ingrese año, tiene que ser menor al ingresado en la primer fecha: "))
                        if year4 < c.getYear():
                            mes4= int(input('Ingrese mes: '))
                            dia4= int(input('Ingrese dia: '))
                            hora4= int(input('Ingrese hora: '))
                            minutos4= int(input('Ingrese minutos: '))
                            segundos4= int(input('Ingrese segundos: '))
                            d= FechaHora(year4,mes4,dia4,hora4,minutos4,segundos4)
                            if d.getYear() != -1:
                                ResultadoResta= c-d
                                print("El resultado de la resta en segundos es: ",ResultadoResta)
                            else:
                                print("La segunda fecha ingresada es incorrecta, por lo tanto no es posible realizar la resta")
                        else:
                            print("No es posible realizar la resta, ya que el segundo año ingresado es mayor o igual al primero")
                    else:
                        print("No es posible realizar la resta ya que la primer fecha ingresada es incorrecta")
                if op == 3:
                    print("\nINGRESE DATOS DE LA PRIMER FECHA A COMPARAR\n")
                    year5= int(input('Ingrese año: '))
                    mes5= int(input('Ingrese mes: '))
                    dia5= int(input('Ingrese dia: '))
                    hora5= int(input('Ingrese hora: '))
                    minutos5= int(input('Ingrese minutos: '))
                    segundos5= int(input('Ingrese segundos: '))
                    e= FechaHora(year5,mes5,dia5,hora5,minutos5,segundos5)
                    if e.getYear() != -1:
                        print("\nINGRESE DATOS DE LA SEGUNDA FECHA A COMPARAR\n")
                        year6= int(input('Ingrese año: '))
                        mes6= int(input('Ingrese mes: '))
                        dia6=int(input('Ingrese dia: '))
                        hora6= int(input('Ingrese hora: '))
                        minutos6= int(input('Ingrese minutos: '))
                        segundos6= int(input('Ingrese segundos: '))
                        f= FechaHora(year6,mes6,dia6,hora6,minutos6,segundos6)
                        if f.getYear() != -1:
                            if e>f:
                                print("La primer fecha ingresada es mayor que la segunda")
                            elif f>e:
                                print("La segunda fecha ingresada es mayor que la primera")
                            else:
                                print("Ambas fechas son iguales")
                        else:
                            print("La segunda fecha ingresada es incorrecta, por lo tanto no es posible comparar las 2 fechas")
                    else:
                        print("No es posible comparar 2 fechas ya que la primer fecha ingresada es incorrecta")
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, Solo puede ingresar numeros del 0 al 3")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
