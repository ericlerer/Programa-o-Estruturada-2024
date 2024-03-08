def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Divisão por zero não é permitida"

def calculadora_cli():
    try:
        num1 = float(input("Informe um número: "))
        num2 = float(input("Informe outro número: "))
        operacao = input("Informe a operação (soma, subtracao, multiplicacao, divisao): ")

        if operacao == "soma":
            resultado = soma(num1, num2)
        elif operacao == "subtracao":
            resultado = subtracao(num1, num2)
        elif operacao == "multiplicacao":
            resultado = multiplicacao(num1, num2)
        elif operacao == "divisao":
            resultado = divisao(num1, num2)
        else:
            resultado = "Operação inválida"

        print(f"Resultado: {resultado}")
    
    except ValueError:
        print("Por favor, insira números válidos.")

calculadora_cli()
