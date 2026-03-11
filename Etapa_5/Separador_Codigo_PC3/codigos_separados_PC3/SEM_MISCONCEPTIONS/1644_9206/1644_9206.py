import numpy as np

def alunos_reprovados(notas):
    # Inicializa o contador de alunos reprovados
   num_reprovados = 0

    # Lista para armazenar os índices dos alunos reprovados
   indices_reprovados = []

    # Percorre as notas para contar e listar os alunos reprovados
   for i in range(len(notas)):
        if notas[i] < 5.0:
            num_reprovados += 1
            indices_reprovados.append(i)

   return num_reprovados, indices_reprovados

def main():
    # Solicita ao usuário as notas dos alunos como uma lista de números reais
   notas = list(map(float, input("Digite as notas dos alunos separadas por espaço: ").split()))

    # Converte a lista de notas para um vetor numpy
   notas = np.array(notas)

    # Chama a função para contar e listar os alunos reprovados
   num_reprovados, indices_reprovados = alunos_reprovados(notas)

    # Exibe o número de alunos reprovados
   print("Número de alunos reprovados:", num_reprovados)

    # Exibe os índices dos alunos reprovados
   print("Índices dos alunos reprovados:", indices_reprovados)

if __name__ == "__main__":
    main()