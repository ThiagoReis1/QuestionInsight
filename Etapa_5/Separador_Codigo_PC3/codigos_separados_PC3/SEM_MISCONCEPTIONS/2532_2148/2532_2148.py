C = input(float("digite o valor: "))
D = input(float("Digite o valor inicial: "))
M = input(float("digite o valor fixo: "))
j = input(float("juros: "))

valor = 40000.0

tempo = D+M*j
if(tempo>valor):
print("dados incorretos")
if(tempo<valor):
print ("dados incorretos")
while(tempo=valor):
print ("dados corretos")

print(C)
print(D)
print(M)
print(j)
