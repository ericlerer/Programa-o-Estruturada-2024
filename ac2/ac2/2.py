def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input("Informe o ano: "))
print(bissexto(ano))
