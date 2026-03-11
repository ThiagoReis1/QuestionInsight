a=int(input("area a ser fertilizada: "))
C =5 #valor por hectare
c= 4 #valor por hectare excedente
if(a<=10000):
	v=C*a
	print(round(v,2))
else:
   v=(a*C-a%10000)
   print(round(v,2))		