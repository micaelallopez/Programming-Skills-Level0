#BANCA ONLINE - Funcionamiento logico 

#INGRESO A LA BANCA

def ingreso_banco(saldo):
    intentos = 0
    while intentos < 3:
        ingreso1 = input ("Ingrese su usuario: ")
        ingreso2 = input ("Ingrese la clave de acceso: ")
        if ingreso1 == username and ingreso2 == password:
            intentos = 3
        intentos = intentos + 1

        if ingreso1 == username and ingreso2 == password:
            print("")
            print("Acceso correcto")
            print("-------------------------------------------------------")
            print(" ")
            print("El saldo en tu cuenta es de: ",saldo)
            print(" ")
        else:
            print("Acceso bloqueado - usuario o clave incorrectos")

def elegir_transaccion(saldo):
    print("----------------------MENÚ-----------------------------")
    print(" 1 - Depositar ")
    print(" 2 - Retirar ")
    print(" 3 - Ver ")
    print(" 4 - Transferir ")
    print(" 5 - Salir ")
    print(" ")
    transaccion = 0
    dep = 0
    ret = 0
    while transaccion <=4:
        transaccion = int(input("Indique el numero de la transacción que desea realizar: "))
        if transaccion == 1:
            depositar = int(input ("Ingrese el monto que desea sumar a su cuenta: "))
            dep = saldo+depositar
            print ("El saldo en su cuenta es de: ",dep)
        elif transaccion == 2:
            retirar = int(input ("Ingrese el monto que desea retirar de su cuenta: "))
            ret = saldo-retirar
            print ("El saldo en su cuenta es de: ",ret)
        elif transaccion == 3:
            print ("El saldo en su cuenta es de: ",saldo)
        elif transaccion == 4:
            transferir = int(input ("Ingrese el monto que desea transferir de su cuenta: "))
            transf = saldo-transferir
            print ("El saldo en su cuenta es de: ",transf)
        else:
            print("Se ha cerrado el menú")
        transaccion = transaccion + 1
        
#Bloque principal
username = input("Registre su usuario: ")
password = input("Registre su clave: ")
print("")
saldo = 2000
ingreso_banco(saldo)
elegir_transaccion(saldo)
