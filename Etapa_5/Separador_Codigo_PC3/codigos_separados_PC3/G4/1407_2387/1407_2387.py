#N varia de 3 a 36
#N = Soma das faces obtidas no sorteio de 3 dados de 12 faces(d1,d2,d3)
qiv = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())

n = d1 + d2 + d3
pr = qiv - 10*n 

if(pr > 0):
	print(pr)
	print("VIVO")
else:
	print("0")
	print("MORTO")	