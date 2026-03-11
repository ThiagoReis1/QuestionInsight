from numpy import*
notas = array(eval(input("insira a nota: ")))
pesos = array([5,1])

num = notas*pesos 
media = (sum(num/(sum(pesos))))
print(round( media, 2))