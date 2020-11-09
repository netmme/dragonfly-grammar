# -*- coding: utf-8 -*-
 
from dragonfly import Text


def strip_input(text):
    diacritic_dico = {
        "é": "e",
        "è": "e",
        "ê": "e",
        "ë": "e",
        "à": "a",
        "â": "a",
        "ô": "o",
        "ù": "u"
    }
    str_text = str(text)
    uni_text = str_text.decode("cp1252").encode("utf-8")
    for key, val in diacritic_dico.items():
        uni_text = uni_text.replace(key, val)

    return uni_text

def snake_case(text):
    """ snake <text> """
    tmp_txt = strip_input(text)
    tmp_txt = tmp_txt.lower()
    output = tmp_txt.replace(" ", "_")
    Text(output).execute()

def camel_case(text):
    """ snake <text> """
    tmp_txt = strip_input(text)
    tmp_txt = tmp_txt.lower()
    output = ""
    caps = True
    for char in tmp_txt:
        if char.isalnum():
            if not caps:
                output += char
            else:
                output += char.upper()
                caps = False
        else:
            caps = True
    Text(output).execute()