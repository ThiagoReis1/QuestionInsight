#Variável Contadora:
c = 0
#Variável de Leitura:
N = int(input("Digite um numero: "))
#Condição de Repetição:
while (N != -1):
   if (35 <= N <= 95):
      c = c + 1
   N = int(input("Digite um numero: "))
#Resultado:
print(c)