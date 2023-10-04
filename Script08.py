# Écrire un programme qui choisi le plus grand nombre parmi deux nombres saisies a partir du clavier

number1= input("veuillez saisir le premier mombre entier\n ")
number2= input("veuillez saisir le deuxieme mombre entier\n ")
if number1> number2:
    print("Le plus grand nombre est: ", number1)
elif number1 == number2:
    print("Les nombres sont égaux!")
else:
    print("Le plus grand nombre est: ", number2)