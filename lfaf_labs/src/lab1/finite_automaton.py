
class Finite_automaton:
    def __init__(self,initial_state,final_states,alphabet,transitions,state):
        self.initial_state = initial_state
        self.final_states = final_states
        self.alphabet = alphabet
        self.transitions = transitions
        self.state = state

    def checkWord(self,word):
        if word[0] not in self.initial_state:
            print("first is false")
            return False

        if word[-1] not in self.final_states:
            print("second is false")
            return  False

        for letter in word:
            if letter not in self.alphabet:
                print("third is false")
                return False

        return True


