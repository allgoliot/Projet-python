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
