#Matheus Gabriel P Campos - 21354618
#16/06/2016
#Avaliação - Exercício 1

a=float(input("Digite o valor do lado A (em metros):"))
b=float(input("Digite o valor do lado B (em metros):"))
c=float(input("Digite o valor do lado C (em metros):"))
val=float(input("Digite o valor do serviço por metros quadrado:"))

per=a+b+c				#perimetro do terreno
custo_total=per*val 	#custo do serviço
y=round(custo_total,2)  
print(y)