### IMPORTER LE MODULE:
# Placer le fichier 'TKInterUtility.py' dans le même dossier que votre programme,
# puis importer le module avec:
import TKInterUtility as util
# Ou avec: import TKInterUtility
# Ou avec: from TKInterUtility import ...


### EXEMPLES D'UTILISATION:
# Donner un nom pour toutes le fenêtres
util.window_title = "Mon programme"


# Afficher quelque chose
util.display("Bonjour!")

# Afficher quelque chose, toutes les options
res = util.display("Bonjour!", # Message à afficher
    canCancel=True, # [False par défaut] Si le bouton 'annuler' est disponible
    continueText="Message pour continuer", # [Optionnel] Massage sur le bouton pour valider
    cancelText="Message pour annuler") # [Optionnel] Massage sur le bouton pour annuler

if res:
    util.display("L'utilisateur a continué")
else:
    util.display("L'utilisateur a annulé")


# Demande du texte (doit etre non vide)
res = util.text_input()
print(res)

# Demande un int
res = util.int_input()
print(res)

# Demande un float
res = util.float_input()
print(res)

# Demande du texte en affichant un autre message
res = util.text_input("Message a afficher à la place de celui par défaut")
print(res)

# Demande du texte, et accepte une valeur vide
res = util.text_input("Message :", acceptempty=True)
print(res)

# Demande du texte avec une condition spéciale
res = util.text_input("Entrez un mot de 5 lettres :", 
    predicate=lambda mot: len(mot)==5)
print(res)

# Demande un int avec une condition spéciale
res = util.int_input("Entrez un entier positif :", 
    predicate=lambda nombre: nombre > 0)
print(res)


# Afficher plusieurs options
res = util.options("Choisissez une option:", ["Option 1:", "Option 2:", "Quitter:"])

if res == 0:
    util.display("L'utilisateur a choisi l'option 1")
elif res == 1:
    util.display("L'utilisateur a choisi l'option 2")
elif res == 2:
    util.display("Au revoir!")
