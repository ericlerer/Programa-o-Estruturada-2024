def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    desconto_irpf = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf
    return salario_liquido

valor_hora = float(input("Informe o valor do salário por hora: "))
num_horas = float(input("Informe o número de horas trabalhadas no mês: "))
salario_liquido = calcula_salario(valor_hora, num_horas)
print(f"O salário líquido é R${salario_liquido:.2f}")