from numpy import*

n=array(eval(input("numero: ")))

cont=zeros(5,dtype=int)

for cont in range(n, 5-1, -1):
	print(cont)
print("Fim da contagem regressiva!")