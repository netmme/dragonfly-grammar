#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dragonfly import Text, Key, MappingRule

class SymbolRules(MappingRule):
    mapping = {
        "slap": Text(" "),
        "quote": Text('"'),
        "dollar": Text("$"),
        "at": Text("@"),
        "logic and": Text("&"),
        "logic or": Text("|"),
        "(diese|hashtag)": Text("#"),
        "open parenthesis": Text("("),
        "close parenthesis": Text(")"),
        "open (brace|bryce)": Text("{"),
        "close (brace|bryce)": Text("}"),
        "list": Text("[]") + Key("left"),
        "deux-points": Text(":"),
        "(mod|modulo|percent)": Text("%%"),
        "(inf|inferior|open chevron)": Text("<"),
        "(sup|superior|close chevron)": Text(">"),
        "(op|operator) equal": Text("="),
        "(assign|affect)": Text(" = "),
        "plus": Text(" + "),
        "(op|operator) plus": Text("+"),
        "minus": Text(" - "),
        "(op|operator) minus": Text("-"),
        "(time|times)": Text(" * "),
        "(op|operator) star": Text("*"),
        "(divided by|slash)": Text("/"),
        "(op|operator) slash": Text("/"),
        "increment": Text("+="),
        "decrement": Text("-="),
        "backslash": Text("\\"),
    }
