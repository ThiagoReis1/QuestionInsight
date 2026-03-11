from math import*

q0=int(input("quantidade inicial: "))
q1=int(input("treinados: "))
q2=int(input("contaminados "))

qt=q0
tri=0

while(qt>0):
	qt=qt+q1-q2
	tri=tri+1
	
print(tri)

