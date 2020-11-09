from dragonfly import MappingRule, Function, Text, Key, Dictation

from .utils.case_type import camel_case, snake_case

def make_block():
     Key("enter").execute()
     Text("{").execute()
     Key("enter:2").execute()
     Text("}").execute()
     Key("up, tab").execute()


class BlockRules(MappingRule):
    mapping = {
         "new main": Text("int main()") + Function(make_block),
         "for loop": Text("for (;;)") + Function(make_block),
         "one line for": Text("for (;;)") + Key("enter, tab, up, end, left:3"),
    }
    extras = [
        Dictation("text")
    ]
