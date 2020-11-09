
from dragonfly import Grammar, CompoundRule, AppContext
from dragonfly.log import setup_log

from generic_grammar.spelling_rules import SpellingRules
from generic_grammar.symbol_rules import SymbolRules
from generic_grammar.writting_rules import WrittingRules
from c_grammar.flux_rules import FluxRules
from c_grammar.keyword_rules import KeywordRules
from c_grammar.generic_rules import GenericRules
from c_grammar.block_rules import BlockRules

setup_log()

class CEnabler(CompoundRule):
    spec = "C on"                  # Spoken command to enable the C grammar.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        cBootstrap.disable()
        cGrammar.enable()
        print("C grammar enabled")

class CDisabler(CompoundRule):
    spec = "C off"                  # spoken command to disable the C grammar.
    
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        cGrammar.disable()
        cBootstrap.enable()
        print("C grammar disabled")

# ===

all_rules = []

symbol_rules = SymbolRules()
all_rules.append(symbol_rules)

spelling_rules = SpellingRules()
all_rules.append(spelling_rules)

writting_rules = WrittingRules()
all_rules.append(writting_rules)

keyword_rules = KeywordRules()
all_rules.append(keyword_rules)

flux_rules = FluxRules()
all_rules.append(flux_rules)

generic_rules = GenericRules()
all_rules.append(generic_rules)

block_rules = BlockRules()
all_rules.append(block_rules)


# The main c grammar rules are activated here
cBootstrap = Grammar("C bootstrap")                
cBootstrap.add_rule(CEnabler())
cBootstrap.load()

cGrammar = Grammar("c grammar")
cGrammar.add_rule(CDisabler())

for rule in all_rules:
    cGrammar.add_rule(rule)

cGrammar.load()
cGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global cGrammar
    if cGrammar: cGrammar.unload()
    cGrammar = None
