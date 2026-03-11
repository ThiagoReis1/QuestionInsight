lambaris=float(input("Populacao inicial de lambaris:"))
tucunare=float(input("Populacao inicial de tucunares:"))
t_l=float(input("Taxa mensal de crescimento de lambaris:"))
t_t=float(input("Taxa mensal de crescimento de lambaris:"))
l= lambaris
t=tucunare
cont=1
while(l >= t):
	la= (l * t_l) + l
	t= (t * t_t) + t	
	cont= cont + 1
	print(cont, l , t)
	