from grammar import Grammar



grammar = {
    'S': ['AC', 'bA', 'B', 'aA'],
    'A': ['e', 'aS', 'ABab'],
    'B': ['a', 'bS'],
    'C':['abC'],
    'D':['AB']
}

g = Grammar(grammar)
g.to_finite_automaton()


# Print the generated string
print("##################################")
print('Generating random words')
generated = g.generate('S')
print(generated)
generated = g.generate('S')
print(generated)
generated = g.generate('S')
print(generated)
generated = g.generate('S')
print(generated)
generated = g.generate('S')
print(generated)

print("##################################")
if g.check_grammar_type():
    print("The grammar is of type 3.")
else:
    print("The grammar is not of type 3.")



