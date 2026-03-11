# faça seu código aqui!
#print("calculo da soma dos cubos de 1 a n")
n=int(input("Digite o valor de n:"))

soma = 0
a=1

while (a<=n):
	
	soma= soma+a**3
	a=a+1


print("soma=",soma)