#Insertable

votes_for_rutra = int(input("Amount of Votes for Rutra: "))
votes_for_olecram = int(input("Amount of Votes for Olecram: "))

#Computation

percentage_of_rutras_votes = round((100*(votes_for_rutra)/((votes_for_rutra)+(votes_for_olecram))),2)
percentage_of_olecrams_votes = round((100*(votes_for_olecram)/((votes_for_rutra)+(votes_for_olecram))),2)

if ((votes_for_rutra) > (votes_for_olecram)):
	print("Ambrosio Rutra")
	print(percentage_of_rutras_votes)
else:
	print("Demelza Olecram")
	print(percentage_of_olecrams_votes)