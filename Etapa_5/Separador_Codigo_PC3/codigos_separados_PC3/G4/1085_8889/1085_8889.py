a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

me = round((a+b+c+d+e)/ 5, 2)
if me >= 6.0:
	print(me)
	print('Aprovacao')
else:
	print(me)
	print ('Reprovacao')