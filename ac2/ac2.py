import math

def eq_seg_grau(a, b, c):
    delta = b**2 - 4*a*c
    raiz1, raiz2 = None, None

    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)

    return raiz1, raiz2

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
c = float(input("Informe o coeficiente c: "))

resultados = eq_seg_grau(a, b, c)

if resultados[0] is not None:
    print(f"A primeira raiz é {resultados[0]}")
    print(f"A segunda raiz é {resultados[1]}")
else:
    print("A equação não possui raízes reais.")

