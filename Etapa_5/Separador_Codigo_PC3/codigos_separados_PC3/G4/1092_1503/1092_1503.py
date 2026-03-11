num = int(input("digite um numero de tres caracteristica:"))

k = num // 100
j = num % 100
l = j//10
l1 = j%10
y = l1

equacao =  ((k**3) + (l**3) + (y**3))

if ( num == equacao ):
	print( num, "atende a propriedade")
else:
	print(equacao)
