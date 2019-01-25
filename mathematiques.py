#Fonction addition
def addition(a,b):
    print("Somme =", a+b)

#Fonction soustraction
def soustraction(a,b):
    print("Soustraction =", a-b)

#Fonction multiplication
def multiplication(a,b):
    print("Multiplication =", a*b)

#Fonction division
def division(a=1,b=1):
    resultat = 0
    try:
        resultat = a/b
        print("Division =",resultat)
    except ZeroDivisionError:
        print('Division par zero impossible !!')
    except TypeError:
        print('Une des deux variable n`est pas un nombre !!')

def demomath():
    addition(10,5)
    soustraction(60,20)
    multiplication(3,5)
    division(6,3)
#demomath()


