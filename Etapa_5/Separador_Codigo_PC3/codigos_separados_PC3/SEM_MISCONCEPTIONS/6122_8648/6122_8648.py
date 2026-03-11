#Variáveis de entrada:
combustivel = float(input("Digite a quantidade de combustivel: "))
#Cálculo e condições:
if (0 < combustivel <= 17.5):
 total = combustivel + 0.8
 print(round(total, 2))
elif (17.5 < combustivel <= 35.0):
 total = combustivel + 1.30
 print(round(total, 2))
elif (35.0 < combustivel <= 50.0):
 total = combustivel + 2.10
 print(round(total, 2))
elif (combustivel > 50.0):
 total = combustivel + 3.0
 print(round(total, 2))
else:
 print("entrada invalida")