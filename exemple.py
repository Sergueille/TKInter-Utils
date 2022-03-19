# Placer le fichier 'TKInterUtility.py' dans le même dossier
# puis importer le module avec:
import TKInterUtility as util
# Ou avec: import TKInterUtility
# Ou avec: from TKInterUtility import ...



# Afficher quelque chose
util.display("Bonjour!")



def annulation():
    print("Annulé!")

# Afficher quelque chose, toutes les options
util.display("Bonjour!", # Message à afficher
    canCancel=True, # [False par défaut] Si le bouton 'annuler' est disponible
    onCancel=annulation, # [Optionnel] Fonction à appeler si annulé
    continueText="Message pour continuer", # [Optionnel] Massage sur le bouton pour valider
    cancelText="Message pour annuler") # [Optionnel] Massage sur le bouton pour annuler

# Note: La fonction arrête le programe jusqu'a la validation
#       Si il y a annulation, les lignes après cette fonction ne seront jamais éxecutées (seulement onCancel sera appelée)



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
# Ou alors: res = InputWindow.text_input(acceptempty=True)
print(res)
