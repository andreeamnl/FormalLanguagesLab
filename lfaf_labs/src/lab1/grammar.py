from finite_automaton import Finite_automaton
import random

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar
        self.terminals = set()
        self.non_terminals = set()
        self.start_symbol = None
        self.parse_grammar()

    def parse_grammar(self):
        for lhs, rhs in self.grammar.items():
            self.non_terminals.add(lhs)
            for symbol in rhs:
                if symbol not in self.non_terminals:
                    self.terminals.add(symbol)

        self.start_symbol = list(self.grammar.keys())[0]

    def generate(self, start_symbol):
            rule = self.grammar.get(start_symbol)
            if rule is None:
                return start_symbol
            else:
                random_rule = random.choice(rule)
                return "".join(self.generate(r) for r in random_rule)

    def to_finite_automaton(self):
        initial_states =[]
        lowercase=[]
        for state in self.grammar['S']:
            initial_states.append(state[0])
            lowercase.append(state[0])
        print("Start state is ", initial_states)

        final_states = []
        for key in self.grammar:
            for state in self.grammar[key]:
                if state.islower():
                    final_states.append(state)
        print("Final states is ", final_states)


        transition_functions = []
        for key in self.grammar:
            for state in self.grammar[key]:
                inter = []
                inter.append(key)
                inter = inter + list(state)
                transition_functions.append(inter)

        print(f'Transitions are: {transition_functions}')

        automaton = Finite_automaton(initial_states,
                                   final_states,
                                   lowercase, ##alphabet
                                   transition_functions,
                                   self.non_terminals)

        #####################################
        #####################################
        ##test input word here
        input_word="cabc"
        if automaton.checkWord(input_word):
            print('Checking input word: ',input_word)
            print('Valid word')
        else:
            print('Checking input word: ',input_word)
            print('Invalid word')
    