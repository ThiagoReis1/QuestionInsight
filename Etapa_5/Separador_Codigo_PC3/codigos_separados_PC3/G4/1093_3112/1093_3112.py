#Entrada
n = int(input("numero qualquer: "))

#separar
cal1 = (n // 100) 
cal2 = (n % 100)

# calculo
cal3 = (cal1 ** 2) + (cal2 ** 2)

#condicao
if (cal3 == n):
	print ("atende") 
	print (n)
else:
	print ("nao atende") 
	print (n)



 

