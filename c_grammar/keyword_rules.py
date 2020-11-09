#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dragonfly import MappingRule, Text, Key


class KeywordRules(MappingRule):
    mapping = {
        "include": Text("#include <>") + Key("left"),
        "math library": Text("math.h"),
        "standard input output library": Text("stdio.h"),
        "float": Text("float "),
        "(int|integer)": Text("int "),
    }
