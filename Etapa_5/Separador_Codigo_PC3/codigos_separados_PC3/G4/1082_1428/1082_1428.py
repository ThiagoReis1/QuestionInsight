n1=float(input("digite a sua primeira nota:"))
n2=float(input("digite a sua segunda nota:"))
n3=float(input("digite a sua terceira nota:"))
n4=float(input("digite a sua quarta nota:"))
n5=float(input("digite a sua quinta nota:"))

soma = float((n1 + n2 + n3+ n4 + n5)/ 5)

if(soma >= 5.0):
	print (round(soma,1)) 
	print ("Aprovado")
else:
	print (round(soma,1))
	print ("Reprovado")
	