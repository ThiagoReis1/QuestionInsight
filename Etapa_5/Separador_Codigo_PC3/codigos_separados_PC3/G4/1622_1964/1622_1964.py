from numpy import*

E = array(eval(input("Digite o numero de entrada de passageiros : ")))
S = array(eval(input("Digite o numero de saida de passageiros : ")))

print(sum(E)-sum(S))
