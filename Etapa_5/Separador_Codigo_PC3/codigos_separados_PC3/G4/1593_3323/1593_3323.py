from numpy import*
a=array(eval(input("Entrada: ")))
cont=0
n=0
for i in range(size(a)):
	cont=cont+((a[i])*(i+1))
	n+=i+1
media=cont/n

print(round(media,2))
	

		  
		  
		  

