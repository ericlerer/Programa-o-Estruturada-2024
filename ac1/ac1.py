import math

def eqsg(a, b, c):

    delta = b**2 - 4*a*c

   
    if delta >= 0:
     
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)


        print(f"A primeira raiz é {raiz1}")
        print(f"A segunda raiz é {raiz2}")
    else:
        print("A equação não possui raízes reais.")


a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))


eqsg(a, b, c)
