a = float(input())
b = float(input())
c = float(input())
d = float(input())

me = (a + b + c + d)/4
me = round(me,2)

if (me >= 7):
	print (me)
	print ("Aprovado")
else:
	print (me)
	print ("Reprovado")