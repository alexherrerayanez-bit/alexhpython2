## ejemplo y uso de while


# def PIN():
#  cont=0
# while cont<=3:
#         print(f"contador {cont}")
#         cont+=1


# pin=3535
# code=int(input("ingrese su pin"))


# while pin!=code:
#         print("Error, intente de nuevo")
#         code=int(input("ingrese su pin "))
#         print("PIN CORRECTO")

#         PIN






## usando el while, pida al usuario un numero
# y muestre su tanla de multiplicar hasta el 10

# num=int(input("ingrese un numero"))
# c=1
# while c<=10:
#     print(f"{num}*{c}={c*num}")
    
#     c+=1


# op=0
# total=0
# while op!=4:
#     print("1.- PC Ryzen $800.000")
#     print("2.- LGTV 55 Pulgadas $450.000")
#     print("3.- Parlante JBL Pure Sounf $90.000")
#     print("4.- salir")
#     print("seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("tiene que pagar", 800000*1.19)
#             total+=800000*1.19
#         case 2:
#             print("tiene que pagar", 450000*1.19)
#             total+=450000*1.19
#         case 3:
#             print("tiene que pagar", 90000*1.19)
#             total+=90000*1.19
#         case 4:
#             print("saliendo")
#             print(f"el total a pagar con IVA es {round(total,2)}")
#         case _:
#             print("opcion invalida")





# #seleccionar 3 programas que ya hemos hecho

# print("1.- sumar")
# print("2.- restar")
# print("3.- muliplicar")
# print("4.- dividir")
# print("5.- salir")

# op=int(input("seleccione una opcion"))

# match op:






# def PromedioNotas():
#     notas = int(input("Ingrese la cant de notas: "))
#     suma=0
#     for i in range(notas):
#         n=float(input(f"Ingrese la nota {i+1}: "))
#         suma=suma+n
#     prom=suma/notas
#     print("El promedio es",round(prom, 1) )

#     if prom>=4:
#         print("ALumno aprobado")
#     else:
#         print("ALumno reprobado")


# def VocalesConsonantes():
#     nombre=input("Ingrese su nombre: ")
#     vocales=0
#     cons=0
#     for i in nombre:
#         print(i)
#         # vocales=vocales+1
#         if i in "aeiou":
#             vocales+=1
#         elif i==" ":
#             print()
#         else:
#             cons+=1
#     print(f"La cant de vocales es {vocales}")
#     print(f"La cant de consonantes es {cons}")
#     VocalesConsonantes


# def PIN():
#     cont=0
#     while cont<=3:
#             print(f"contador {cont}")
#             cont+=1
#     pin=3535
#     code=int(input("ingrese su pin"))
#     while pin!=code:
#             print("Error, intente de nuevo")
#             code=int(input("ingrese su pin "))
#             print("PIN CORRECTO")
#             PIN()



        

# op=0
# total=0
# while op!=4:
#     print("1.- opcion 1")
#     print("2.- opcion 2")
#     print("3.- opcion 3")
#     print("4.- salir")
#     print("seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             PromedioNotas ()
            
#         case 2:
#             VocalesConsonantes ()
            
#         case 3:
#             (PIN)
            
#         case 4:
#             print("saliendo")
#             print(f"inente mas tarde",)
#         case _:
#             print("opcion invalida")



# Votatoon

toon1=input("ingrese toon 1")
toon2=input("ingrese toon 2")

v1=0
v2=0
cant=int(input("cuantos votantes son?"))

while cant>0:
    voto=int(input(f"por quien votara? 1.- {toon1} 2.- {toon2} "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("voto nulo")
    cant-=1
if v1>v2:
    print(f"Gano {toon1} con {v1} votos")
elif v2>v1:
    print(f"Gano {toon2} con {v1} votos")