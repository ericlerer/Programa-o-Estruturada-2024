def calcula_media(ap1, ap2, as_, ac):

    menor_ap = min(ap1, ap2)
    media_sem_as = (ap1 + ap2) * 0.4 + ac * 0.2

    if as_ > menor_ap:
        media_com_as = (as_ + ap2) * 0.4 + ac * 0.2
    else:
        media_com_as = (as_ + ap1) * 0.4 + ac * 0.2

    return max(media_sem_as, media_com_as)

def verifica_aprovacao(media):
    return "Aprovado" if media >= 7.0 else "Reprovado"

def main():
    nome = input("Digite seu nome: ")
    if not nome:
        print("Programa encerrado.")
        return
    ap1 = float(input("Digite a nota da AP1: "))
    ap2 = float(input("Digite a nota da AP2: "))
    as_ = float(input("Digite a nota da AS: "))
    ac = float(input("Digite a nota da AC: "))

    media_final = calcula_media(ap1, ap2, as_, ac)

    print(f"A média final de {nome} é: {media_final:.2f}")

    resultado = verifica_aprovacao(media_final)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
