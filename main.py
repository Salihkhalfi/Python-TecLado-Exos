
print("##################### INPUT() #########################################")

user_age = int(input("Entrer votre âge : "))
months = user_age * 12
days = user_age * 365

print(f"Votre âge comporte {months} mois, ou {days} jours !!!")

print()

# ############# LES LISTES TUPLES  SETS #################################################################

print("##################### LES TUPLE, LISTE, SET #########################################")

list_names = ["Salah", "Bob", "Amar", "Kadour"]
# on ne peut pas modifier les elts dans un tuple
tuple_names = ("Salah", "Bob", "Amar", "Kadour")
set_names = {"Salah", "Bob", "Amar", "Kadour"}

list_names[1] = "Martine"
list_names = ["Salah", "Bob", "Amar", "Kadour"]
print(f"List_names devient : {list_names}")

list_names.insert(1, "Grégory")  # Insertion à la  place de Martine
print(f"List_names devient : {list_names}")

list_names.append("Khalfi")
print(f"List_names devient : {list_names}")

list_names.remove("Amar")
print(f"List_names devient : {list_names}")

list_names.pop()  # supprime le dernier elt
print(f"List_names devient : {list_names}")

list_names.pop(2)  # supprime "Bob"
print(f"List_names devient : {list_names}")

set_names.add("eric")  # l'ordre n'intervient pas dans un Set
print(f"List_names devient : {set_names}")

set_names.add("Salah")  # on peut dupliquer les elts d'un set
print(f"List_names devient : {set_names}")

# ############### Union, intersection, difference en set  ########

friends = {"Grégory", "Eric", "Ahmed", "Abdel"}
abroad = {"Amar", "Bob", "Eric"}

differ_friends = friends.difference(abroad)
print(f"La différence entre les 2 sets : {differ_friends}")

union_friends = friends.union(abroad)
print(f"L'union des 2 sets : {union_friends}")

intersec_friends = friends.intersection(abroad)
print(f"L'intersection des 2 sets : {intersec_friends}")

print()

print("##################### EXERCICE TUPLE, LISTE, SET #########################################")

######################  EXERCICE  #################################
# This coding exercise requires you to complete three steps:
#
# Create a list, called my_list, with three numbers. The total of
# the numbers added together should be 100.
# Create a tuple, called my_tuple, with a single value in it
# Modify the variable set2  so that set1.intersection(set2)
# returns {5, 77, 9, 12}
# set1 = {14 , 5 , 9 , 31 , 12 , 77 , 67 , 8}
# set2 = {5}
###################################################################

# Création de la liste my_list dont la somme des elts est égale à 100

my_list = [50, 30, 20]

# Création de my_tuple avec un seul elt
my_tuple = (73, )  # Si on met (73) my_tuple ne sera pas considéré comme tuple

set1 = {14, 5, 9, 31, 12, 77, 67, 8}

# On modifie les elts de set2 pour avoir l'intersection ===> {5, 77, 9, 12}
# set2 doit contenir ses elts ci-dessous
set2 = {5, 77, 9, 12}

# Modify the variable set2  so that set1.intersection(set2)
# returns {5, 77, 9, 12}

new_set2 = set1.intersection(set2)
# l'affichage nous donne des elts non triés
print(f"Le nouveau contenu de set2 est de : {new_set2}")

# On va afficher le new_set2 avec des elts triés
# l'affichage nous donne des elts non triés
print(f"Le nouveau contenu de set2 trié est de : {sorted(new_set2)}")

print()

# ############# Les booléens ############################################################
print("##################### lES BOOLEANS #########################################")


print(5 == 5)  # True
print(5 > 5)   # False
print(5 != 5)  # False

print(f"le set friends est égal abroad ? : {friends == abroad}")
# ====> False
# le '==' compare les elts des deux sets

# le 'is' compare si c'est la m^me valeur en mémoire,
# et ne compare pas les elts des sets ou des listes ou des tuples

# avec "is"====> False
print(f"le set friends est égal abroad avec 'is' ? : {friends is abroad}")

print()

################# LES STATEMENTS ############################################################
print("##################### lES STATEMENTS #########################################")

# Mettre en  minuscule
day_of_week = input("quel jour sommes-nous cette semaine ? : ").lower()

if day_of_week == "vendredi":
    print(f"nous sommes le Vendredi")
else:
    print(f"Erreur !, nous sommes pas le {day_of_week}")

print("Good Bye !!!!!!!!!!!!")

# ################ LE IN ###############################################################

last_names = ["ralf", "engy", "boubakeur", "salah"]

personne = ""
while personne == "":

    personne = input("Qui se trouve dans notre réseau d'amitié ? : ").lower()
    if personne == "":
        continue  # On continue dans la boucle pour éviter d'afficher
        # Dommage " " n'est pas dans notre réseau snif snif
    elif personne in last_names:
        print(f"Super {personne} est dans notre réseau")
    else:
        print(f"Dommage {personne} n'est pas dans notre réseau snif snif ...")
print()

################# LES  BOUCLES #############################################################
print("###################### LES BOUCLES ###########################################################")

friends_list = ["Ralf", "engy", "boubakeur", "salah"]

for friend in friends_list:
    print(f"{friend} est mon ami !")

grades = [35, 67, 98, 100]
total = 0  # la somme des elts de la liste grades

for grade in grades:
    total += grade

print(f"la somme des {len(grades)} elts de la liste grades = {total}")

##################### AVEC SUM #################################################################################################

total = sum(grades)

amount = total / len(grades)

print(f"le montant des {len(grades)} elts de la liste grades = {amount}")

print()

################################# EXERCICE ########################################
# This coding exercise has two steps.
#
# Modify the code so that the evens list contains only the even numbers of the
# numbers list. You do not need to print anything.
# For part 2, add a clause to the if statement such that if the user's input is "q",
# your program prints "Quit".
# Remember that for these coding exercises, Python will care about uppercase and
# lowercase letters, so make sure to use the right ones!
#
# -- Part 1 --
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# evens = []
# for number in numbers:
#     evens.append(number)
# -- Part 2, must be completed before submitting! --
# user_input = input("Enter your choice: ")
# if user_input == "a":
#     print("Add")
########################### EXERCICE ############################################
print("#################### EXERCICE #############################################")

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []  # La liste des nobres pairs
odd = []    # La liste des nombres impaires

for number in numbers:
    if number % 2 == 0:  # Trouver les nombres pairs
        evens.append(number)  # Les insérer dans la liste evens
    elif number % 2 != 0:  # nombre impairs
        odd.append(number)  # On insère le nombre dans la liste odd impaire

print(f"La liste des nombres pairs est : {evens}")
print(f"La liste des nombres impairs est : {odd}")

# -- Part 2, must be completed before submitting! --
user_input = input("Entrez votre choix: a (Add), q (Quit) : ").lower()
if user_input == "a":
    print("Ajouter")
elif user_input == "q":
    print("Quit")

else:
    print("mauvaise réponse !!!")

print()

##################### LIST  COMPREHENSION #################################################################################################

print("################## LIST COMPREHENSION ####################################")

numbers = [1, 5, 77, 99, 45]
doubled_list = []  # On insère chaque elt  mutiplié par 2

doubled_list = [item * 2 for item in numbers]

print(f"doubled_list en liste comprehension est égale à : {doubled_list}")

friends = ["Rolf", "Sam", "Samantha", "Salah", "Tamara", "Kaki"]

# On crée une liste des elts qui commencent par "s"
start_with_s = [friend for friend in friends if friend.startswith("S")]

print(
    f"la liste comprehension des elts qui commencent par 'S' est : {start_with_s}", end="\n" * 2)
# end = "\n" * 2  ===> Saut de 2 lignes

#################### LES IDs DES LISTE EN MEMOIRE ##############################
# l'id est l'adresse de la liste en mémoire

print(
    f"l'id en mémoire de friends est : {id(friends)} de start_with_s : {id(start_with_s)}")

print()

####################### LES DICTIONNAIRES #################################################################

print("################### LES DICTIONNAIRES ######################################")

print()

friend_ages = {"Salah": 56, "Ralf": 25, "Sam": 23, "Tamara": 21, "Kaki": 12}
friend_ages["Sara"] = 20

print(f"le nouveau dictionnaire devient : {friend_ages}")

print("l'âge de Tamara est : ", friend_ages["Tamara"])

# ################Imprimer les Clés et les valeurs ##########################

print(f"Les clés de friend_ages sont : {friend_ages.keys()}")
print(f"Les valeurs de friend_ages sont : {friend_ages.values()}")

##################### Impression en liste ###################################

print("##################### Impression en liste ###################################")

print(f"Les clés de friend_ages en liste : {list(friend_ages.keys())})")
print(f"Les valeurs de friend_ages en liste: {list(friend_ages.values())}")

##################### Impression des items () ###################################

print("##################### Impression des items () ###############################")

print(f"impression des items de friend_ages : {friend_ages.items()}")

print(f"impression des items de friend en liste : {list(friend_ages.items())}")

##################### LISTE DES DICTIONNAIRES #######################################

print("##################### LISTE DES DICTIONNAIRES ################################")

friends = [

    {"nom": "Salah", "age": 56},
    {"nom": "Amar", "age": 38},
    {"nom": "Sara", "age": 20},
    {"nom": "Eric", "age": 35}

]

################### imprimer "Sara" ###################################################################
print("imprimer le 2ème elt de la liste dict : ",
      friends[2]["nom"], ", agé(e) de : ", friends[2]["age"], " ans .")

################### afficher avec items avec une boucle ###############################################

students = {"Salah": 56,
            "Amar": 38,
            "Sara": 20,
            "Eric": 35
            }

for nom, age in students.items():
    print(f"les elts du Dictionary avec items : {nom} agé(e) de : {age} ans.")

################ On peut imprimer aussi sous forme d'une liste de Tuple #############

print(f"students devient une liste de tuples : {list(students.items())}")

########################  Ont peut aussi l'écrire ligne par ligne ############################

for item in students.items():
    print(f"Etudiant : {item} ans.")

# ############# Est qu'une personne est avec les etudiants ? #########################################

print("############# Est qu'une personne est avec les etudiants ? ##################################")

personne = input("Qu'elle personne cherche tu ? : ")

if personne.capitalize() in students:
    print(f"Youpiiii , {personne} est dans le près des étudiants")
else:
    print(f"Mince !!! , {personne} n'est pas dans le près des étudiants")

#################### Calculer la moyenne d'age des etudiants #############################

moyenne_age = sum(students.values()) // len(students)
# On peut aussi écrire :
# moyenne_age = round(sum(students.values()) / len(students))

print(f"La moyenne d'âge des étudiants est de : {moyenne_age} ans.")

print()

#################  LA DESTRUCTURATION  ##############################################

print("#################  LA DESTRUCTURATION  ######################################")

print()

tete, *queue = [1, 4, 5, 7, 100, 200, 300, 400, 500, 600, 700, 800]

print(f"la tête contient : {tete}, la queue contient : {queue}")

######### Aussi on peut écrire  ####################################################

*tete, queue = [1, 4, 5, 7, 100, 200, 300, 400, 500, 600, 700, 800]

print(f"la tête devient : {tete}")
print(f"la queue devient : {queue}")

print()
