#UFAM 
#pedro paulo almeida da costa- 21602333
num= int(input("digite um numero de três digitos"))
# "a" é o primeiro digito
a = num // 100
ra = num % 100
# "b" é o segundo digito
b = ra //10
# "c" é o terceiro digito
c = ra % 10
if (num == (a**3)+(b**3)+(c**3) ):
	print(num,"atende a propriedade")
else:
	print((a**3)+(b**3)+(c**3))