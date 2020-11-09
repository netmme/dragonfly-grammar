# -*- coding: utf-8 -*-

from dragonfly import MappingRule, Text


class SpellingRules(MappingRule):
    mapping = {
        "agent": Text("a"),
        "bath": Text("b"),
        "cap": Text("c"),
        "drum": Text("d"),
        "each": Text("e"),
        "fine": Text("f"),
        "gust": Text("g"),
        "hello": Text("h"),
        "sit": Text("i"),
        "jury": Text("j"),
        "krunch": Text("k"),
        "look": Text("l"),
        "made": Text("m"),
        "near": Text("n"),
        "odd": Text("o"),
        "pit": Text("p"),
        "quench": Text("q"),
        "roast": Text("r"),
        "sun": Text("s"),
        "trap": Text("t"),
        "you": Text("u"),
        "vest": Text("v"),
        "wagon": Text("w"),
        "plex": Text("x"),
        "yank": Text("y"),
        "zip": Text("z")
    }
