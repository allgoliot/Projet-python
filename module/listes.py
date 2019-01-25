def nb_elements(liste):
	compte=0
	for mot in liste:
		compte+=1
	return compte

def afficher_la_liste(liste):
	print(liste)

def ajouter_dans_liste(liste, element):
	if not element in liste:
		liste.append(element)

def remplace(liste,element1,element2):
	index=0
	if element1 in liste:
		liste[index]=element2
	else:
		index+=1

def supprime(liste,element):
	liste.remove(element)

def demoliste():
	ma_liste= ["element1","element2","element3"]
	print("la liste contient",nb_elements(ma_liste)," elements")
	afficher_la_liste(ma_liste)
	
	print("jajoute element 4 dans la liste",ajouter_dans_liste(ma_liste,"element4"))
	afficher_la_liste(ma_liste)

	print("je remplace element1 par tutu")
	remplace(ma_liste,"element1","tutu")
	afficher_la_liste(ma_liste)

	print("je suprime tutu de ma liste")
	supprime(ma_liste,"tutu")
	afficher_la_liste(ma_liste)

def creerliste():
	fin=0
	cpt=1
	liste=[]
	while fin == 0:
		message="element n°"+str(cpt)+" de la liste (champ vide=stop) : "
		entree=input(message)
		if entree != "":
			liste.append(entree)
			cpt+=1
		else:
			fin=1
	return liste

def menuliste():
	fin=0
	liste=[]
	while fin == 0:
		print("---Menu de la mort !---")
		print("- 0. Creer une liste auto")
		print("- 1. Compter le nb d\'element d\'une liste (la creer si vide)")
		print("- 2. Afficher la liste")
		print("- 3. Ajouter un element en fin de liste")
		print("- 4. Remplacer un element de la liste par un autre")
		print("- 5. Supprimer un element de la liste")
		print("- 6. Demo de liste.py")
		print("- *. Fin")
		print("-----------------------")
		choix=input("Votre choix : ")
		if choix=="0": #creation liste auto
			print("----")
			if liste == []:
				print("Création !")
				liste= ["element1","element2","element3"]
			print("----\n")
		elif choix=="1": #Compter le nb d\'element d\'une liste
			print("----")
			if liste == []:
				print("Liste est vide\nCréation !")
				liste=creerliste()
				print("Il y a ",nb_elements(liste)," element dans votre liste")
			else:
				print("Il y a ",nb_elements(liste)," element dans votre liste")
			print("----\n")
		elif choix=="2":#Afficher la liste
			print("----")
			if liste == []:
				print("Liste est vide\nCréation !")
				liste=creerliste()
				afficher_la_liste(liste)
			else:
				afficher_la_liste(liste)
			print("----\n")
		elif choix=="3":#Ajouter un element en fin de liste
			print("----")
			if liste == []:
				print("Liste est vide\nCréation !")
				liste=creerliste()
				print("Done")
			else:
				ajouter_dans_liste(liste,input("Element à ajouter : "))
				afficher_la_liste(liste)
			print("----\n")
		elif choix=="4":#remplacer un element de la liste par un autre
			print("----")
			if liste == []:
				print("Liste est vide\nCréation !")
				liste=creerliste()
				print("done")
				afficher_la_liste(liste)
				remplace(liste,input("Element à rempacer : "),input("Entrer le nouvel element : "))
				afficher_la_liste(liste)
			else:
				remplace(liste,input("Element à rempacer : "),input("Entrer le nouvel element : "))
				afficher_la_liste(liste)
			print("----\n")
		elif choix=="5":#Supprimer un element de la liste
			print("----")
			if liste == []:
				print("Liste est vide\nCréation !")
				liste=creerliste()
				print("done")
				afficher_la_liste(liste)
				supprime(liste,input("Element à supprimer : "))
				afficher_la_liste(liste)
			else:
				afficher_la_liste(liste)
				supprime(liste,input("Element à supprimer : "))
				afficher_la_liste(liste)
			print("----\n")
		elif choix=="6":#Demo de liste.py
			demoliste()
		else:
			print("Aucun choix")
			print("Fin du programme")
			fin = 1

#menuliste()
