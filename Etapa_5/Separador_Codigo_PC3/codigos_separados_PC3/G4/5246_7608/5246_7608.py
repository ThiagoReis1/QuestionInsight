
i = int(input(""))
p = float(input(""))
if 0 <= i and i <= 130 and 0.0 <= p and p <= 550.0 :
	if i <= 20 and p <= 60 :
		print("Grupo de risco: 9")
	else :
		if i <= 20 and 90 >= p > 60 :
			print("Grupo de risco: 8")
		else :
			if i <= 20 and 90 < p :
				print("Grupo de risco: 7")
			else :
				if 20 < i <= 50 and p <= 60 :
					print("Grupo de risco: 6")
				else :
					if 20 < i <= 50 and 90 >= p > 60 :
						print("Grupo de risco: 5")
					else :
						if 20 < i <= 50 and 90 < p :
							print("Grupo de risco: 4")
						else :
							if i > 50 and p <= 60 :
								print("Grupo de risco: 3")
							else :
								if i > 50 and 90 >= p > 60 :
									print("Grupo de risco: 2")
								else :
									print("Grupo de risco: 1")
else :
	print("Dados invalidos")




