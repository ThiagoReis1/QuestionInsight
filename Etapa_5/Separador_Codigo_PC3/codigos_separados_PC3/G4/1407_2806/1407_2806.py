var= int(input("Digite quantidade inicial de pontos de vida: "))
d1= int(input("Digite valores de d1: "))
d2=int(input("Digite valores de d2: "))
d3=int(input("Digite valores de d3: "))

numb=  12 * d1 + d2 + d3
a=var - numb

if (a > 0):
	print(a)
	print ("VIVO") 

else:
	print (a)
	print ("MORTO")

