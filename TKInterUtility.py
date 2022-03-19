from tkinter import *
from tkinter import ttk
import asyncio

# FONCTIONS INTERNES

class InputWindow:
    def _on_submit(self, _):
        self.result = self.entry.get()
        self.root.destroy()

    def __init__(self, message):
        self.result = None

        self.root = Tk()
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
    def __init__(self, message, canCancel, continueText, cancelText, onCancel):
        self.ended = False   

        self.root = Tk()
        frm = ttk.Frame(self.root, padding=5)
        frm.grid()
        
        ttk.Label(frm, text=message).grid(column=0, row=0, columnspan=2)

        def _on_submit():
            self.ended = True
            self.root.destroy()

        def _onCancel():
            self.root.destroy()
            onCancel()
        
        ttk.Button(frm, text=continueText, command=_on_submit).grid(column=0, row=1, pady=5)
        if canCancel:
            ttk.Button(frm, text=cancelText, command=_onCancel).grid(column=1, row=1, pady=5, padx=5)

        self.root.mainloop()


async def _display_async(message, canCancel, continueText, cancelText, onCancel):
    window = InfoWindow(message, canCancel, continueText, cancelText, onCancel)

    while not window.ended:
        pass

# FONCTIONS EXTERNES

def text_input(message = "Entrez du texte :", acceptempty=False):
    """
    Demande tu texte a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Maessage affiché sur la fenêtre
            Par défaut: "Entrez du texte :"
        acceptempty (bool, optional): 
            Est-ce que l'utilisateur peut ne rien entrer
            Par défaut: False

    Returns:
        str: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "str", acceptempty))

def float_input(message = "Entrez un nombre à virgule :"):
    """
    Demande un float a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Maessage affiché sur la fenêtre
            Par défaut: "Entrez un nombre à virgule :"

    Returns:
        float: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "float"))

def int_input(message = "Entrez un entier :"):
    """
    Demande un int a l'utilisateur avec une fenêtre

    Args:
        message (str, optional): 
            Maessage affiché sur la fenêtre
            Par défaut: "Entrez un entier :"

    Returns:
        int: La valeur entrée par l'utilisateur
    """
    return asyncio.run(_text_input_async(message, "int"))

def display(message, canCancel=False, continueText="Ok!", cancelText="Annuler", onCancel = None):
    """
    Affiche quelque chose dans une fenêtre

    Args:
        message (str): 
            Maessage affiché sur la fenêtre
        canCancel (bool, optional): 
            Est-ce que le bouton annuler est disponible
            Par défaut: False
        continueText (str, optional): 
            Texte affiché sur le bouton pour valider
            Par défaut: "Ok!"
        cancelText (str, optional): 
            Texte affiché sur le bouton pour annuler
            Par défaut: "Annuler"
        onCancel (callable, optional): 
            Fonction a appeler si l'utilisateur appuie sur annuler
    """
    asyncio.run(_display_async(message, canCancel, continueText, cancelText, onCancel))
