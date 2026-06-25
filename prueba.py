# print("Hola Osvaldo")  

# # creando variables

# titulo="Clima de hoy"  # String
# diaDelMes=13  # int
# mes=4       #int

# temperatura=22.3 # float

# llueve=False # boolean

# print(titulo)
# print("Temperatua actual:", temperatura, "grados")
# print(diaDelMes, "-", mes)

# # "rojo"=="verde" ---->False
# # 7>3 ---> True
# if llueve:  
#     print("Tiene que llevar paraguas")
# else:
#     print("puede llevar polera sin mangas")


# # pedir password y pin
# # Pida al usuario password en palabra que debe ser "temu"
# # ademas pida el pin que debe ser 3435
# # los dos deben estar correctos para acceder al sistema

#passw="temu"


# for i in "Alex":
#  print (i)

# # pregunte al usuario su nombre y muestra sus letras
# print ("ingrese nombre")
# name=input()
# nombre=input("ingrese su nombre")



# SIN ARGUMENTO Y CON RETORNO

# suma()
# def sumaRet():
#     n1=int(input("ingrese un numero: ")
#     n2=int(input("ingrese otro numero: "))
#     return n1+n2
# res=sumaRet()*4
# print("el resultado es", res)

# CON ARGUMENTO Y SIN RETORNO

# def saludoME(name):
#     print("hola", name)

# saludoME("Hola Alex")




pinturas=[
    {"color": "azul", "capacidad": 5000, "formato": "tarro"},
    {"color": "verde", "capacidad": 2500, "formato": "aerosol"},
    {"color": "rojo", "capacidad": 3000, "formato": "bolsa"}
]





def funcion(lista, color ):
    c=input("que color busca?: ")
    for p in lista:
        if funcion == color:
            return print("disponible")
        else: 
            return print("el color no  esta disponible", color)
        
cae1=input("que color va a elegir?: ")

funcion(pinturas,cae1)




def mostrarpinturas():
    if len(pinturas)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.-{p}")










