from tkinter import *
from tkinter import ttk

# VARIABLES GLOBALES
window_title = "python"


# FONCTIONS

class InputWindow:
    def _on_submit(self):
        self.result = self.entry.get()
        self.root.destroy()

    def __init__(self, message, error_message=""):
        self.result = None

        self.root = Tk()
        self.root.title(window_title)
        self.root.after(1, lambda: self.root.focus_force())
        frm = ttk.Frame(self.root, padding=5)
        frm.grid()
        
        ttk.Label(frm, text=message).grid(column=0, row=0, padx=5)

        if error_message != "":
            ttk.Label(frm, text=error_message, foreground="#FF0000").grid(column=0, row=1, pady=5, columnspan=3)

        self.entry = ttk.Entry(frm)
        self.entry.grid(column=1, row=0, padx=5)
        self.entry.focus()
        
        ttk.Button(frm, text="Envoyer", command=self._on_submit).grid(column=2, row=0, padx=5)
        self.root.bind('<Return>', lambda _: self._on_submit())# add function on enter
        self.root.mainloop()

def _text_input_internal(message, type, acceptempty=False, predicate=None, error_message=""):
    window = InputWindow(message, error_message)

    while window.result == None:
        pass

    if type == "str":
        if acceptempty or len(window.result.strip()) > 0:
            parsedRes = window.result
        else:
            return _text_input_internal(message, type, acceptempty, predicate, error_message="Veuillez entrer une valeur non vide.")
    
    try:
        if type == "int":
            parsedRes = int(window.result)
        elif type == "float":
            parsedRes = float(window.result)
        elif type != 'str':
            raise Exception("Unknown type")
    except ValueError:
        return _text_input_internal(message, type, acceptempty, predicate, error_message="Valeur incorrecte, réessayez.")

    if predicate != None and not predicate(parsedRes):
        return _text_input_internal(message, type, acceptempty, predicate, error_message="Valeur incorrecte, réessayez.")

    return parsedRes


class InfoWindow:
    def __init__(self, message, canCancel, continueText, cancelText):
        self.result = None   

        self.root = Tk()
        self.root.title(window_title)
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()

        def _on_submit():
            self.result = True
            self.root.destroy()

        def _onCancel():
            self.result = False
            self.root.destroy()
        
        ttk.Button(frm, text=continueText, command=_on_submit).grid(column=0, row=1, pady=5)
        if canCancel:
            ttk.Button(frm, text=cancelText, command=_onCancel).grid(column=1, row=1, pady=5, padx=5)
            ttk.Label(frm, text=message).grid(column=0, row=0, columnspan=2)
        else: 
            ttk.Label(frm, text=message).grid(column=0, row=0, columnspan=1)

        self.root.mainloop()


def display(message, canCancel=False, continueText="Ok!", cancelText="Annuler"):
    """
    Affiche quelque chose dans une fenêtre

    Args:
        message (str): 
            Message affiché sur la fenêtre
        canCancel (bool, optional): 
            Est-ce que le bouton annuler est disponible
            Par défaut: False
        continueText (str, optional): 
            Texte affiché sur le bouton pour valider
            Par défaut: "Ok!"
        cancelText (str, optional): 
            Texte affiché sur le bouton pour annuler
            Par défaut: "Annuler"

    Retourne:
        bool: Si l'utilisateur a validé ou annulé
    """
    window = InfoWindow(message, canCancel, continueText, cancelText)

    while window.result == None:
        pass

    return window.result

class OptionWindow:
    def __init__(self, message, list):
        self.selected = None

        self.root = Tk()
        self.root.title(window_title)
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        
        ttk.Label(frm, text=message).grid(column=0, row=0, columnspan=2)

        def _on_submit(selected):
            self.selected = selected
            self.root.destroy()

        for i in range(len(list)):
            ttk.Label(frm, text=list[i]).grid(column=0, row=i+1, pady=2)
            ttk.Button(frm, text=">", command=lambda a=i: _on_submit(a), width=2).grid(column=1, row=i+1, pady=2)

        self.root.mainloop()


def options(message, list):
    """
    Affiche plusieurs options sous forme de boutons à l'utilisateur

    Args:
        message (str): 
            Message affiché en haut de la fenêtre
        list (list): 
            liste des noms des options

    Retourne:
        int: L'id de l'option sélectionnée
    """

    window = OptionWindow(message, list)

    while window.selected == None:
        pass

    return window.selected

# VARIANTES INPUT

def text_input(message = "Entrez du texte :", acceptempty=False, predicate=None):
    """
    Demande tu texte a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez du texte :"
        acceptempty (bool, optional): 
            Est-ce que l'utilisateur peut ne rien entrer
            Par défaut: False
        predicate (callable, optional):
            Fonction qui renvoie un bool qui détermine si la valeur est correcte

    Retourne:
        str: La valeur entrée par l'utilisateur
    """
    return _text_input_internal(message, "str", acceptempty, predicate)

def float_input(message = "Entrez un nombre à virgule :", predicate=None):
    """
    Demande un float a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez un nombre à virgule :"
        predicate (callable, optional):
            Fonction qui renvoie un bool qui détermine si la valeur est correcte

    Retourne:
        float: La valeur entrée par l'utilisateur
    """
    return _text_input_internal(message, "float", predicate=predicate)

def int_input(message = "Entrez un entier :", predicate=None):
    """
    Demande un int a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez un entier :"
        predicate (callable, optional):
            Fonction qui renvoie un bool qui détermine si la valeur est correcte

    Retourne:
        int: La valeur entrée par l'utilisateur
    """
    return _text_input_internal(message, "int", predicate=predicate)
