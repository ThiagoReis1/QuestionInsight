from numpy import*

vetor = array(eval(input("Informe os valores: ")))

vetor2 = [1,3,2,5]

multiplicacao = vetor * vetor2 

a = sum(multiplicacao)
b = sum(vetor2)

print(round(a /b, 2))