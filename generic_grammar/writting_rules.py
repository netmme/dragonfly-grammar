from dragonfly import MappingRule, Text, Key, Dictation, Function

def snake_case(text):
    tmp_txt = text.lower()
    output = tmp_txt.replace(" ", "_")
    Text(output).execute()

def burger_case(text):
    tmp_txt = text.lower()
    output = tmp_txt.replace(" ", "-")
    Text(output).execute()

def camel_case(text):
    tmp_txt = text.lower()
    txt_list = tmp_txt.split(" ")
    camel_list = [word[0].upper() + word[1:] for word in txt_list]
    output = "".join(camel_list)
    Text(output).execute()

class WrittingRules(MappingRule):
    mapping = {
        "snake <text>": Function(snake_case, text="&(text)s"),
        "camel <text>": Function(camel_case, text="&(text)s"),
        "burger <text>": Function(burger_case, text="&(text)s"),
    }
    extras = [
        Dictation("text")
    ]
