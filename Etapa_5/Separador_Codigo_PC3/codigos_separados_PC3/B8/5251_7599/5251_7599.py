des = input("cidade:")
idade = int(input("idade:"))
if((des=="porto velho") or (des=="santarem") or (des=="belem") or (des=="tefe") or (des=="tabatinga")) and ((0<=idade) and (idade<=150)):
	if(des=="porto velho"):
		if(idade<=2):
			print("Passagem: R$ 0.0")
		else:
			if(3<=idade<=12):
				x = 500/2
				print("Passagem: R$",round(x,2))
			else:
				if(65<=idade):
					x = 500*(70/100)
					print("Passagem: R$",round(x,2))
				else:
					x = 500
					print("Passagem: R$",round(x,2))
	else:
		if(des=="santarem"):
			if(idade<=2):
				print("Passagem: R$ 0.0")
			else:
				if(3<=idade<=12):
					x = 370/2
					print("Passagem: R$",round(x,2))
				else:
					if(65<=idade):
						x = 370*(70/100)
						print("Passagem: R$",round(x,2))
					else:
						x = 370
						print("Passagem: R$",round(x,2))
		else:
			if(des=="belem"):
				if(idade<=2):
					print("Passagem: R$ 0.0")
				else:
					if(3<=idade<=12):
						x = 600/2
						print("Passagem: R$",round(x,2))
					else:
						if(65<=idade):
							x = 600*(70/100)
							print("Passagem: R$",round(x,2))
						else:
							x = 600
							print("Passagem: R$",round(x,2))
			else:
				if(des=="tefe"):
					if(idade<=2):
						print("Passagem: R$ 0.0")
					else:
						if(3<=idade<=12):
							x = 360/2
							print("Passagem: R$",round(x,2))
						else:
							if(65<=idade):
								x = 360*(70/100)
								print("Passagem: R$",round(x,2))
							else:
								x = 360
								print("Passagem: R$",round(x,2))
				else:
					if(des=="tabatinga"):
						if(idade<=2):
							print("Passagem: R$ 0.0")
						else:
							if(3<=idade<=12):
								x = 550/2
								print("Passagem: R$",round(x,2))
							else:
								if(65<=idade):
									x = 550*(70/100)
									print("Passagem: R$",round(x,2))
								else:
									x = 550 
									print("Passagem: R$",round(x,2))
else:
	print("Entradas invalidas")