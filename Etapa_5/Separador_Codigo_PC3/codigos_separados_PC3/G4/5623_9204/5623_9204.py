a = input("digite o item escolhido (B/S):").upper()
e = int(input("digite a quantidade de (B/S):"))
c = int(input("digite a quantidade de cappuccinos:"))


if a=="B":
	soma = (e*5.00)+ (c*7.50)
else:
	soma = (e*4.00)+(c*7.50)
print(round(soma,2))
