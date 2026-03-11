# pedindo a quantidade de dias 
dias = int(input("Quantidade de dias utilizara o equipamento?: "))

total = (dias*50.00 + 30.00) # calculando o total sem o ICMS
total = total + (total*(18/100))	# total com o imposto
print(round(total, 2)) # imprimindo o custo total
