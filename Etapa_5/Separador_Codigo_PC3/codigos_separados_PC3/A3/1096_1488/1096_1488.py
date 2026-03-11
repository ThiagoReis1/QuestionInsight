n = int(input("Digite um numero: "))
  
v1 = n // 100000
resto1 =  v1 % 100000
v2 = v1 // 10000
resto2 = resto1 % 1000
v3 = resto2 // 100
resto3 = resto2 % 100

soma = v1**3 + v2**3 + v3**3
 
if(soma == n):
	  print(n,"atende a propriedade")
 
else:
	  print(soma)


