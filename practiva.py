#nombre=input("ingrese su nombre: ")
#n_letras=0
#for i in nombre:
   # print(i)
   # n_letras=n_letras+1
   # print("el numero de letras de su nombre es:", n_letras)
  

print("ingrese su nombre")
name=input()
vocales=0
consonantes=0
for i in name:
    print(i)
    if i in "aeiouAEIOU":
        vocales=vocales+1
    elif i=="":
        ""
    else:
         consonantes=consonantes+1
        print("la cantidad de vocales son {vocales}")
        print("el numero de consonantes son {consonantes}")

