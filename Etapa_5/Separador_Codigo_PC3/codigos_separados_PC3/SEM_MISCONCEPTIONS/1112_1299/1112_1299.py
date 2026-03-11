#ADRIANO CARELLI
#AV - 03

salario = float(input("Digite o salario: "))


print("Entradas:", salario)

if(salario > 0):
        if(salario <= 800):
                valor = salario * 
        elif(salario <= 1000):
                valor = salario * 0.40
        if(salario <= 1200):
                valor = salario * 0.30
        elif(salario <= 1400):
                valor = salario * 0.20
        if(salario <= 1600):
                valor = salario *0.10
        elif(salario > 1600):
                valor = salario * 

else:
        salario = -1
if(salario != -1):
        print("Valor total: R$", round(valor, 2))
else:
        print("Dados invalidos")