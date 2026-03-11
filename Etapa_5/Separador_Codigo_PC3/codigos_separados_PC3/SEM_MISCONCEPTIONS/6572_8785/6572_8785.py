# faça seu código aqui!
n_p= int(input())
fixo= 5


if n_p < 3:
	valor= n_p * fixo + 3
elif n_p == 3:
	valor= n_p * fixo + 3.25
else:
	valor= n_p * fixo + 4.5

print('total=',round(valor,2))