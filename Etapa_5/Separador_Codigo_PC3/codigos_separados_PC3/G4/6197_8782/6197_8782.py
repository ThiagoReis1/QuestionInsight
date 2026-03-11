alta = 1.6
taa = 0.02
anos=0
a= float(input(" sua altura: "))
tx=float(input(" taxa de crescimento: "))
while a < alta:
	alta+=taa
	a+=tx
	anos+=1
print(anos)