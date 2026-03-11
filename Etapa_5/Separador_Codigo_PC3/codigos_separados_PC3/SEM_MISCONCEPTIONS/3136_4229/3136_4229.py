from numpy import*
vetor = array(eval(input("N numeros reais: ")))
M = (exp(vetor)*log(vetor))/vetor
print(round(M,2))