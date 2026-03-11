e = array(eval(input("informe: ")))
i = 0
cont = 0
while(i < e):
	if(e[i] <= 75):
		e[i] = e[i] - e[-1]
	i = i + 1