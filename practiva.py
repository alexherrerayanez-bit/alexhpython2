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











numeros=input("ingrese numeros enteros separados por espacio: ")

listaNumeros=numeros.split()
listanumerosint=[]

pares=[]
impares=[]

for n in listaNumeros:
    listanumerosint.append(int(n))
    print(n)

for hh in listanumerosint:
    if hh%2==0:
        pares.append(hh)
    else:
        impares.append(hh)
print(f"los numeros pares son {pares}")
print(f"los numeros impares son {impares}")

    
