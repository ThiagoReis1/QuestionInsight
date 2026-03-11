from numpy import*
#Vetor de entrada
vetor = array(eval(input("Digite o valor do dado: ")))
#Variáveis contadoras e acmuladoras:
pontos = 0
i = 0
#Laço
while i < size(vetor):
   if (vetor[i] == 1):
      pontos += 10
   if (vetor[i] == 2):
      pontos += 5
   if (vetor[i] == 3):
      pontos += 10
   if (vetor[i] == 4):
      pontos += 5
   if (vetor[i] == 5):
      pontos += 10
   if (vetor[i] == 6):
      pontos += 5
   i += 1
#Resultado
print(pontos)
