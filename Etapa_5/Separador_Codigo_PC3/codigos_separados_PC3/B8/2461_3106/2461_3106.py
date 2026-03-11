custo = float(input("Digite o valor do preco de custo: "))

if (custo <= 50):
	margem = custo * 2

elif(50.01 <= custo <= 100):
	margem = custo + (custo/2)

elif(100.01 <= custo <= 500):
	margem = custo + (custo * 0.4)
	
elif(custo > 500):
	margem = custo + (custo * 0.3)
	
print(round(margem,2))