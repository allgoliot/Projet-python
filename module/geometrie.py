# operations perimetre et surface : cercle, rectangle, carré

import math

def perimetre_cercle():
	rayon=float(input("Veuillez saisir le rayon: " ))
	l= 2*math.pi*rayon
	print(l) 

def perimetre_rectangle():
	longueur = float(input("Veuillez saisir le longueur: " ))
	largeur = float(input("Veuillez saisir le largeur: " ))
	l=2*longueur + 2*largeur
	print(l)

def perimetre_carre():
	cote = float(input("Veuillez saisir le côté: " ))
	l=4*cote
	print(l)

def surface_cercle():
	rayon=float(input("Veuillez saisir le rayon: " ))
	s= math.pi*rayon*rayon
	print(s)

def surface_rectangle():
	longueur = float(input("Veuillez saisir le longueur: " ))
	largeur = float(input("Veuillez saisir le largeur: " ))
	s=longueur*largeur
	print(s)

def surface_carre():
	cote = float(input("Veuillez saisir le côté: " ))
	s=cote**2
	print(s)

def menugeo():
	retour=0
	while retour == 0:
		print("--- Choisir une fonction---")
		print("1. perimetre_cercle")
		print("2. perimetre_rectangle")
		print("3. perimetre_carre")
		print("4. surface_cercle")
		print("5. surface_rectangle")
		print("6. surface_carre\n")
		print("tout autre entrée pour arrêter le programme")
		choix=input("Votre choix : ")
		if choix=="1":
			perimetre_cercle()
		elif choix=="2":
			perimetre_rectangle()
		elif choix=="3":
			perimetre_carre()
		elif choix=="4":
			surface_cercle()
		elif choix=="5":
			surface_rectangle()
		elif choix=="6":
			surface_carre()
		else:
			print("Aucun choix")
			print("Fin du programme")
			retour = 1

