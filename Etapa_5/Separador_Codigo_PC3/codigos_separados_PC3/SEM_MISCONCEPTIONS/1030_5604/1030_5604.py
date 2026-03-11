minuto= float(input("digite os minutos excedentes: "))

plano = 45.00
excedente= 0.97 * minuto
valor= (plano + excedente)
porcentagem = valor * 42/100
total= valor + porcentagem


print(round(total, 2))