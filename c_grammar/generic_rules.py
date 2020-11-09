
from dragonfly import MappingRule, Text, Key, Function, Dictation

from .utils.case_type import camel_case, snake_case


class GenericRules(MappingRule):
    mapping = {
        "(Termine | Hermine)": Key("end") + Text(";") + Key("enter"),
        "snake <text>": Function(snake_case, text="%(text)s"),
        "camel <text>": Function(camel_case, text="%(text)s"),
        "phrase <text>": Text('"%(text)s"')
    }
    extras = [
        Dictation("text")
    ]