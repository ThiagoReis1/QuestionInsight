salario = float(input("Insira o salario: "))
if(0 < salario <= 800):
  aumento = (salario * 50)/ 100
  total = salario + aumento
  print("Entrada: R$", salario)
  print("Novo salario: R$", round(total, 2))
elif (800 < salario <= 1000):
  aumento = (salario * 40)/ 100
  total = salario + aumento
  print("Entrada: R$", salario)
  print("Novo Salario: R$", round(total, 2))
elif (1000 < salario <= 1200):
 aumento = (salario * 30)/ 100
 total = salario + aumento
 print("Entrada: R$", salario)
 print("Novo Salario: R$", round(total, 2))
elif (1200 < salario <= 1400):
 aumento = (salario * 20)/ 100
 total = salario +aumento
 print("Entrada: R$", salario)
 print("Novo Salario: R$", round(total, 2))
elif (1400 < salario <= 1600):
 aumento = (salario * 10)/ 100
 total = salario + aumento
 print("Entrada: R$", salario)
 print("Novo Salario: R$", round(total, 2))
elif (salario > 800):
 aumento = (salario * 5)/ 100
 total = salario + aumento
 print("Entrada: R$", salario)
 print("Novo Salario: R$", round(total, 2))
else:
  print("Entrada: R$", salario)
  print("Dado invalido")
  

