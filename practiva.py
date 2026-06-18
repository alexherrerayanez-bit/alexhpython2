#nombre=input("ingrese su nombre: ")
#n_letras=0
#for i in nombre:
   # print(i)
   # n_letras=n_letras+1
   # print("el numero de letras de su nombre es:", n_letras)
  



# print("ingrese su nombre")
# name=input()
# vocales=0
# consonantes=0
# for i in name:
#     print(i)
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#     elif i=="":
#         ""
#     else:
#          consonantes=consonantes+1
#         print("la cantidad de vocales son {vocales}")
    
#         print("el numero de consonantes son {consonantes}")


# import random

# num=random.randint(1,9)

# while abs(-3)!=num:
#    print(num)
#    time.sleep(1)

#    num=random.randint(1,9)

# n1=int(input("ingrese el valor del limite inferior"))
# n2=int(input("ingrese el valor del limite superior"))
# while n2 <= n1:
#     print("el limite superior no es mayor que el inferior")
#     n2 = int(input("ingrese el valor del limite superior: "))
# print("parametros correctos")
# num=random.randint(n1,n2)
# print(num)


# plancha=0
# lata=0
# peso= random.randint(800,3000)
# peces= random.randint(10,20)
# print("salio un total de peces de:", peces)
# print("el total de peso de peces es:", peso)
# for i in range (peces):
#     peso = random.randint(500, 3000)
#     if peso<=800:
#        lata += 1
#     elif peso >= 801 and peso <= 3000:
#         plancha += 1
#     else: 
#         print("peso invalido")

# print(f"el total de peces en latas son {lata}")
# print(f"el total de peces en plancha son {plancha}")






# frutas=["naranja", "frutilla", "kiwi", "melon", "frambuesa"]

# for f in frutas:
#     if f[-1].lower() == "a":
#         print(f"la fruta {f} termina con a")
#     else: 
#         print(f"la fruta {f} no termina con a")



# juguetes=["yo-yo", "tetris"]

# def agregar():
#     ju=input("Agregue un juguete: ")
#     juguete.append(ju)

# def mostrar():
#     c=1
#     for j in juguetes:
#         c=1
#         print(j,c)
#         c+=1
#         print("-"*30)

# def actualizar():
#     print("que juguete desea actualizar: ")
#     act=int(input())
#     nuevojug=input("Ingrese nuevo juguete: ")
#     juguetes[act-1]=nuevojug


# def eliminar():
#     eliminar=int(input("Que juguete desea eliminar: "))
#     juguetes.pop(eliminar-1)
#     print("juguete eliminado")



# def menuJuguetes():
# while True:
#         try:
#             print("1.- Agregar juguete")
#             print("2.- Eliminar juguete")
#             print("3.- Actualizar juguete")
#             print("4.- Mostrar juguetes")
#             print("5.- salir")
#             op=int(input("seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
                    
#                 case 2:
#                     eliminar()
                    

#                 case 3:
#                     actualizar()

                    
#                 case 4:
#                     mostrar()
#                 case 5:
#                     ("saliendo")
#                     break
#                 case _:
#                     ("error")
        

#         except Exception as e:
#             print("error :", e)











# numeros=input("ingrese numeros enteros separados por espacio: ")

# listaNumeros=numeros.split()
# listanumerosint=[]

# pares=[]
# impares=[]

# for n in listaNumeros:
#     listanumerosint.append(int(n))
#     print(n)

# for hh in listanumerosint:
#     if hh%2==0:
#         pares.append(hh)
#     else:
#         impares.append(hh)
# print(f"los numeros pares son {pares}")
# print(f"los numeros impares son {impares}")




# productosDicc={
#    1:{"nombre": "Maracuyá", "precio": 3000},
#    2:{"nombre": "Pera", "precio": 1500},
#    3:{"nombre": "Cebolla", "precio": 1200}
# }
# productosDicc[4]={"nombre": "Piña", "precio": 3500}
# def agregarProducto():
#    print("Cual es el nombre del producto?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())[-1]
#    productosDicc[nuevoKey+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#       print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    borrar=int(input("Cual Producto borrará?: "))
#    del productosDicc[borrar]
# def actualizarProducto():
#    MostrarProducto()
#    num=int(input("Que producto desea actualizar?: "))

#    nombre=input("Cual es el nombre nuevo?: ")
#    precio=int(input("Cual es el precio nuevo?: "))
#    productosDicc[num]={"nombre": nombre, "precio": precio}





# while True:
#     def compra():
#         mostrarproducto()
#         try:
#             com=int(input("que producto va a comprar?: "))
#             if com in productosDicc.keys():
#                 carrito.append(productosDicc[com])
        
#         except Exception as e:
#             print("error:", e)




# peliculasGOD={
#     1:{"nombre": "ElCaballeroOscuro", "precio": 5000},
#     2:{"nombre": "ElPadrino", "precio": 4000},
#     3:{"nombre": "OtroDiaParaMatar", "precio": 7000}
# }
# def agregarPelicula():
#     print("Cual es el nombre de la pelicula?: ")
# nombre = input()
# print("Cual es el precio?: ")






# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°'''
# Para que este grave debe tener mas de 39°
# Cada atencion vale $25.000
# Los despcuentos corresponden a 
# FOnasa 54%
# Isapre 27%
# Fodesa 12,5%


pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre", 
    "temperatura":39.6, "grave": True})




def validarEstado(tempe):
    if tempe>39:
       return True 
    else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
    for p in pacientes:
        print(f"{c} .- {p}")
        c+=1
def agregarPaciente():
    nombre=input("Ingrese nombre: ")
    prevision=input("Ingrese prevision: ")
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
            "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")
    def eliminarPaciente():
     mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci-1)
    print("Paciente eliminado.")
    def tomarTemp():
     mostrarPacientes()
    paciente=int(input ("A que paciente le tomamos temperatura?: "))
    tomarTemp=float(input("ingrese su temperatura: "))
    pacientes[paciente-1]["temperatura"]=tomarTemp
    pacientes[paciente-1]["grave"]=validarEstado(tomarTemp)
    def cobrarAtencion():
     mostrarPacientes()
    pa=int(input("¿que paciente va a pagar?: "))
    if pacientes[pa-1]["prevision"].lower()=="fonasa":
        pagar=25000*0.46
    elif pacientes[pa-1]["prevision"].lower()=="isapre":
        pagar=25000*0.73
    elif pacientes[pa-1]["prevision"].lower()=="fodesa":
        pagar=25000*0.875
    else:
        print("prevision incorrecta")
        print("Su total a pagar es: ", pagar)
































while True: 
    try:
     print("1.- Agregar Paciente")
     print("2.- Quitar Paciente")
     print("3.- Tomar temperatura")
     print("4.- Cobrar Paciente")
     print("5.- Mostrar Paciente")
     print("6.- Salir")

     match op:
        case 1:
           eliminarpaciente()
           
        case 2:
           print()
        
        case 3:
           mostrarPacientes()
           p=int(input("a que paciente le tomara la temperatura?: "))
           T=float(input("ingrese nueva temperatura: "))
           pacientes[p-1]["temperatura"]=T
           
        
        case 4:
           print()
           
        case 5:

        
     

    except Exception as e:
       print("error: ", e)
