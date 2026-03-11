x= float(input("qual a quantidade inicial de pontos de vida:"))
d1= int(input("qual o valor do dado d1:"))
d2= int(input("qual o valor do dado d2:"))
d3= int(input("qual o valor do dado d3:"))
 
n= 10* ((d1+d2+d3 >= 3) and (d1+d2+d3 <= 36))
y= (x-n)

if (y > 0):
	print (("vivo") .upper)
elif (y < 0):
	print (("morto") .upper)