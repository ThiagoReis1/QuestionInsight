ax = float(input("altura de aluno: "))
tx = float(input("taxa crescimento aluno: "))
al= 1.65
tl= 0.02
c = 0

while( ax< al):
	ax = ax + tx
	al = al + tl
	c = c +1
print(c)
