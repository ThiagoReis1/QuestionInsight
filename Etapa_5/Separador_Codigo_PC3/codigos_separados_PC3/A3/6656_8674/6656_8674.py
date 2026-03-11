from numpy import*

# peso das motas [3,4,2,1,4,5]
notas = array(eval(input()))
pesos = [3,4,2,1,4,5]

total = 0
i = 0 

a = pesos * notas 
b = sum(a)
c = b / sum(pesos)
print(round(c, 2))