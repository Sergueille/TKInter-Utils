from tkinter import *
from tkinter import ttk
import asyncio

# VARIABLES GLOBALES
window_title = "python"

# FONCTIONS INTERNES

class InputWindow:
    def _on_submit(self, _):
        self.result = self.entry.get()
        self.root.destroy()

    def __init__(self, message):
        self.result = None

        self.root = Tk()
        self.root.title(window_title)
        frm = ttk.Frame(self.root, padding=5)
        frm.grid()
        
        ttk.Label(frm, text=message).grid(column=0, row=0, padx=5)

        self.entry = ttk.Entry(frm)
        self.entry.grid(column=1, row=0, padx=5)
        self.entry.focus()
        
        ttk.Button(frm, text="Envoyer", command=self._on_submit).grid(column=2, row=0, padx=5)
        self.root.bind('<Return>', self._on_submit)# add function on en
        self.root.mainloop()

async def _text_input_async(message, type, acceptempty=False):
    window = InputWindow(message)

    while window.result == None:
        pass

    if type == "str":
        if acceptempty or len(window.result.strip()) > 0:
            return window.result
        else:
            return await _text_input_async("Veullez entrer une valeur non vide :", type)
    
    try:
        if type == "int":
            return int(window.result)
        elif type == "float":
            return float(window.result)
        else:
            raise Exception()
    except ValueError:
        return await _text_input_async("Valeur incorrecte, réessayez :", type)

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


async def _display_async(message, canCancel, continueText, cancelText):
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

async def _options_async(message, list):
    window = OptionWindow(message, list)

    while window.selected == None:
        pass

    return window.selected

# FONCTIONS EXTERNES

def text_input(message = "Entrez du texte :", acceptempty=False):
    """
    Demande tu texte a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez du texte :"
        acceptempty (bool, optional): 
            Est-ce que l'utilisateur peut ne rien entrer
            Par défaut: False

    Retourne:
        str: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "str", acceptempty))

def float_input(message = "Entrez un nombre à virgule :"):
    """
    Demande un float a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez un nombre à virgule :"

    Retourne:
        float: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "float"))

def int_input(message = "Entrez un entier :"):
    """
    Demande un int a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Message affiché sur la fenêtre
            Par défaut: "Entrez un entier :"

    Retourne:
        int: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "int"))

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
    asyncio.run(_display_async(message, canCancel, continueText, cancelText))

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

    return asyncio.run(_options_async(message, list))
