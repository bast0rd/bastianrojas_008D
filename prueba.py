import time
import os
import random
import csv


bl = "─" * 36
contador = True
pedido = []
sector = ("San Bernardo", "Calera de Tango", "Buin")
sector_guardado = ('san_bernardo','calera_tango','buin')
sct = []
numero = 0
saco5 = 0
saco5tr = "0"
saco10 = 0
saco10tr = "0"
saco20 = 0
saco20tr = "0"
nada = ("Nro.ped", "Cliente", "Dirrecion", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg")
nada_str = "      ".join(nada)

existe = os.path.exists('ruta_de_pedido.csv')
if existe == True:
    os.system("cls")
elif existe == False:
    #ruta de pedido
    with open('ruta_de_pedido.csv', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(nada)
    #ruta de San Bernardo
    with open('san_bernardo.txt', 'w') as archivo:
        archivo.write(nada_str + '\n')
    #ruta calera
    with open('calera_tango.txt', 'w') as archivo:
        archivo.write(nada_str + '\n')
    #ruta buin
    with open('buin.txt', 'w') as archivo:
        archivo.write(nada_str + '\n')
    
    
def borrar(b):
    time.sleep(b)
    os.system("cls")
    
def menu():
    global contador
    while contador == True:
        print(f"bienvenido a la tienda de comida de gatos, selecione una opcion \n{bl}")
        print(f"1) registrar pedido \n2) lsitar todos los pedidos \n3) imprimir hoja de ruta \n4) salir del programa")
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print("error en la seleccion")
            borrar(1)
            continue
        if eleguir in [1,2,3,4]:
            borrar(0.5)
            return(eleguir)
        else:
            print("no es una opcion")
            borrar(1)
    
def cliente():
    global contador
    while contador == True:
        print(f"ingrese el nombre de usuario para el pedido \n{bl}")
        nombre = input("──> ")
        apelldio = input("ahora su apellido \n──> ")
        nombre_apellido = nombre + " " + apelldio
        borrar(0.5)
        while contador == True:
            print(f"seguro que ese es tu nombre? ──> {nombre_apellido} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s", "S"]:
                pedido.append(nombre_apellido)
                contador = False
                borrar(0.5)
            elif eleguir in ["n","N"]:
                print("volviendo a ingresar nombre.")
                borrar(0.5)
                break
            else:
                print("no es una opcion")
                borrar(1)
    contador = True

def dirrecion():
    global contador
    while contador == True:
        print(f"profavor ingrese su direccion \n{bl}")
        dirreciones = input("──> ")
        borrar(0.5)
        while contador == True:
            print(f"esta bien esta dirrecion? ──> {dirreciones} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                pedido.append(dirreciones)
                contador = False
                borrar(0.5)
            elif eleguir in ["n","N"]:
                print("volviendo a ingresar dirrecion.")
                borrar(0.5)
                break
            else:
                print("no es una opcion.")
                borrar(0.5)
    contador = True
            
def sectores():
    global contador , numero
    while contador == True:
        print(f"ingrese uno de los sectores en las que va a pedir \n{bl}")
        for i in sector:
            numero += 1
            print(f"{numero}) {i}")
            time.sleep(0.2)
        numero = 0
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print("error en la opcion.")
            borrar(1)
            continue
        if eleguir in [1,2,3]:
            eleguir -= 1
            pedido.append(sector[eleguir])
            sct.append(sector_guardado[eleguir])
            borrar(0.5)
            break
        else:
            print("no es una opcion")
            borrar(1)
    
def menu_pedidos():
    global contador
    while contador == True:
        print(f"seleccione una de estas para agregar al pedido \n{bl} \nactual pedido: saco 5kg = {saco5} | saco 10kg = {saco10} | saco 20kg = {saco20} \n{bl}")
        print(f"1) saco de 5kg \n2) saco de 10kg \n3) saco de 20kg \n4) confirmar pedido")
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print("error en la selecion.")
            borrar(1)
            continue
        if eleguir in [1,2,3,4]:
            borrar(0.5)
            return(eleguir)
        else:
            print("no es una opcion.")
            borrar(1)
    
def saco_5kg():
    global contador, saco5, saco5tr
    while contador == True:
        print(f"ingrese la cantidad del pedido del saco de 5kg \n{bl}")
        try:
            numero = int(input("──> "))
        except ValueError:
            print("no es un numero")
            borrar(1)
            continue
        while contador == True:
            print(f"estas seguro que desea ingresar esta cantidad? ──> {numero} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                saco5 += numero
                saco5tr = str(saco5)
                contador = False
                borrar(0.5)
            elif eleguir in ["n","N"]:
                print("volviendo a eleguir la cantidad.")
                borrar(0.5)
                break
    contador = True
    
def saco_10kg():
    global contador, saco10, saco10tr
    while contador == True:
        print(f"ingrese la cantidad del pedido del saco de 10kg \n{bl}")
        try:
            numero = int(input("──> "))
        except ValueError:
            print("no es un numero")
            borrar(1)
            continue
        while contador == True:
            print(f"estas seguro que desea ingresar esta cantidad? ──> {numero} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                saco10 += numero
                saco10tr = str(saco10)
                contador = False
                borrar(0.5)
            elif eleguir in ["n","N"]:
                print("volviendo a eleguir la cantidad.")
                borrar(0.5)
                break
    contador = True

def saco_20kg():
    global contador, saco20, saco20tr
    while contador == True:
        print(f"ingrese la cantidad del pedido del saco de 20kg \n{bl}")
        try:
            numero = int(input("──> "))
        except ValueError:
            print("no es un numero")
            borrar(1)
            continue
        while contador == True:
            print(f"estas seguro que desea ingresar esta cantidad? ──> {numero} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                saco20 += numero
                saco20tr = str(saco20)
                contador = False
                borrar(0.5)
            elif eleguir in ["n","N"]:
                print("volviendo a eleguir la cantidad.")
                borrar(0.5)
                break
    contador = True
    
def guardar():
    global pedido, sct, saco5,saco10,saco20
    with open('ruta_de_pedido.csv','a',newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(pedido)
    
    pedido_str = "     ".join(pedido)
    with open(f'{sct}.txt','a') as archivo:
        archivo.write(pedido_str + '\n')
        
    pedido.clear
    sct.clear
    
while contador == True:
    x = menu()
    if x == 1:
        c = random.randint(1,1000)
        c_tr = str(c)
        pedido.append(c_tr)
        cliente()
        dirrecion()
        sectores()
        while contador == True:
            x = menu_pedidos()
            if x == 1:
                saco_5kg()
            elif x == 2:
                saco_10kg()
            elif x == 3:
                saco_20kg()
            elif x == 4:
                pedido.append(saco5tr)
                pedido.append(saco10tr)
                pedido.append(saco20tr)
                guardar()
                break
    elif x == 2:
        with open('ruta_de_pedido.csv', 'r', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            for i in lector_csv:
                print(i)
        #este input solo sirve como pausa
        input("aprete cualquier tecla àra volver....")