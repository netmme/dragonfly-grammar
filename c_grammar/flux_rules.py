
from dragonfly import MappingRule, Text, Key


class FluxRules(MappingRule):
    mapping = {
            "print F": Text("printf();") + Key("left:2"),
            "scan F": Text("scanf();") + Key("left:2"),
    }
