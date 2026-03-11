from numpy import*

notas= array(eval(input()))
i=0

p1=2
p2=2
p3=6
p4=1

p1=p1*notas[0]
p2=p2*notas[1]
p3=p3*notas[2]
p4=p4*notas[-1]

np=(p1+p2+p3+p4)/(2+2+6+1)
print(round(np,2))