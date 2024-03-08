def dia_semana(numero):
    if 1 <= numero <= 7:
        dias_semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
        return dias_semana[numero - 1]
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2)) 
    print(dia_semana(6)) 
    print(dia_semana(7))  
    print(dia_semana(9))  

testa_dia_semana()
