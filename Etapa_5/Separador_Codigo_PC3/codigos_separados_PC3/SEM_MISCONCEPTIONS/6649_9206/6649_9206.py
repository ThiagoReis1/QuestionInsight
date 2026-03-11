import numpy as np

# Vetor de pesos
pesos = [3, 2, 4, 1, 3]

# Entrada do vetor de notas
vetor_notas = eval(input("Digite as notas separadas por vírgulas e entre colchetes: "))

# Verifique se o tamanho do vetor de notas é o mesmo que o vetor de pesos
if len(vetor_notas) == len(pesos):
    # Calcula a média ponderada
   media_ponderada = np.dot(vetor_notas, pesos) / sum(pesos)
    
    # Imprime a média ponderada arredondada para duas casas decimais
    print(round(media_ponderada, 2))
else:
    # Se os tamanhos dos vetores forem diferentes, imprime uma mensagem de erro
   print("Os tamanhos dos vetores de notas e pesos são diferentes.")