al = float(input("altura de um pessoa: "))
tx = float(input("taxa de crescimento: "))
ab= 1.69
tb = 0.01
c = 0 #anos ate que o aluno seja maior que Bia

while(al < ab):
	ab = ab + tb
	al = al + tx
	c = c + 1
print(c)
