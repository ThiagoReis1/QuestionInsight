# Quantidade de miniutos excedentes 
q = float(input("quantidade de minutos excedentes: "))

#FORMULA PARA CALCULAR O VALOR A SER PAGO

var = 45+0.97*q

valor = var + (var*0.42)

print(round(valor,2))