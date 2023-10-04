# Écrire un programme qui va trouver le plus grand nombre parmi 3 nombres saisis a partir du clavier

number1= int(input("veuillez saisir le premier mombre entier\n "))
number2= int(input("veuillez saisir le deuxieme mombre entier\n "))
number3= int(input("veuillez saisir le 3ème mombres entiers\n "))

if number1> number2 and number1> number3:
    print("Le plus grand nombre est: ", number1)
elif number2> number3 :
    print("Le plus grand nombre est: ", number2)
else:
    print("Le plus grand nombre est: ", number3)