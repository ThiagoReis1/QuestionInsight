x = int(input("Insira o valor desejado de tres digitos: "))
n1 = x // 100
resto1 = x%100
n2 = resto1 // 10
resto2 = resto1%10
n3 = resto2
soma_cubos = (n1**3) + (n2**3) + (n3**3)
if (soma_cubos == x):
 print(x,"atende a propriedade")
else:
 print(soma_cubos)