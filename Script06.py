# Décire un programme qui va lire les données d'un employé a partir du clavier
# identifiant, nom, salaire, adresse, marié

id= int(input("veuillez entrer votre identifiant"))
nom= input("veuillez entrer votre nom")
salaire= float(input("veuillez entrer votre salaire"))
adresse= input("veuillez entrer votre adresse")
status= bool(input("est ce que vous êtes marié?[True|False]"))
print("SVP, confirmer vos informations personnelles")
print("Le nom de l'employé est : ", nom)
print("Le ID de l'employé est: ", id)
print("Le salaire de l'employé est : ", salaire)
print("L'adresse' de l'employé est : ", adresse)
print("Est ce que l'employé est marié: ", status)


