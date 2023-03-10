# Laboratory work no. 2 report.
### Course: Formal Languages & Finite Automata
### Student: Andreea Manole,  FAF-212 
### Task 15

## Objectives:
1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
## Implementations:
2. For the first task we have to add some functionality to differ between grammar types, so i decided to implement a method for the **Grammar** class that outputs a boolean True if the grammar is in fact of type 3.
    There's some rules we must follow to carefully detect what we look for:

            a. The start symbol can only appear on the left side of a production rule.

            b. Each production rule can have only one non-terminal symbol on the left-hand side.

            c. The right-hand side of each production rule must consist of a single terminal symbol or a single non-terminal symbol followed by a terminal symbol.

            d. Production rules can be of two types:
                Non-terminal symbol → ε (where ε represents the empty string).
                Non-terminal symbol → terminal symbol or Non-terminal symbol.

    Here is my implementation:
    
![screenshot](screenshots/gr1.png)

## Results
![screenshot](screenshots/gr2.png)

3. Objectives

    a. We must convert FA to RG.
        Here we mostly play with existing FA transitions from the **Finite_automaton** class. For each transition we add a new rule to the grammar, this can be done easily by checking the length of the transition list (3 elements or 2) and adding a functionality for both cases in the conversion. Also mostly appending and concatenating was done here.
        Also the output is a dictionary, because my ***Grammar*** class accepts a dictionary as input. Therefore this is the desired output *for my code*.

    Here is my implementation:
    ![screenshot](screenshots/farg1.png)

    ## Results
    ![screenshot](screenshots/farg2.png)

    b. Determine whether your FA is deterministic or non-deterministic.
    To determine whether an FA is an NFA or DFA, you need to check the following:


        Determine if the FA has multiple transitions on the same input symbol from a state. If it does, then it is an NFA.

        Check if there is any state with an epsilon transition to another state. If there is, then it is an NFA.

        Verify if every state in the FA has exactly one transition on each input symbol in the alphabet. If this is the case, then it is a DFA.

        Check whether the FA accepts strings by final state or by empty stack. If it accepts by final state only, then it is a DFA.


    For my implementation I've decided it's easier and faster to check if automaton is of type NFA, by identifying whether I encounter any multiple transitions with same input symbol of a state (check if current symbol exists in my symbol list (called ```counts```)), once this happens the return of the method automatically becomes False.

    Here is my implementation:
    ![screenshot](screenshots/dfa_or_nfa.png)

    ## Results
    ![screenshot](screenshots/aut2.png)


    c. Implement some functionality that would convert an NDFA to a DFA.
    First of all my FA is definitely deterministic, so in my case I would implement this for a *potential* NFA. figured I culd also put my *fa_type* method for good use and have it dictate whether this method should be called or not. Now, for the method itself, we must follow some rules first:

        Start with the initial state of the NDFA as the initial state of the DFA.

        Create a new state in the DFA for each combination of states that the NDFA can be in after reading a particular input symbol.

        For each new state in the DFA, determine which states of the NDFA it represents. This can be done by tracing all possible paths through the NDFA from the initial state, following the transitions for the input symbol.

        For each new state in the DFA, determine its transitions by considering all possible transitions from the states it represents in the NDFA. If there are multiple transitions for a single input symbol, combine them into a single transition in the DFA.

        Mark any state in the DFA that includes an accepting state of the NDFA as an accepting state of the DFA.

        Repeat steps 2-5 for each input symbol until all states in the DFA have been created and transitions determined.

        The resulting DFA represents the same language as the original NDFA.

    Here is my *part* of implementation:
    ![screenshot](screenshots/conv1.png)
    ![screenshot](screenshots/conv2.png)

 
    d. Represent the finite automaton graphically 
    I've decided to use this tool I found on *http://magjac.com/graphviz-visual-editor/*.
    Here is the code provided.
    
    ![screenshot](screenshots/visual1.png)

    Here is the output:

    ![screenshot](screenshots/visual2.png)


---
## Conclusions
In conclusion, the study of finite automata, grammar types, NFA, and DFA provides important insights into the theory and practice of computational science. Through laboratory work, we have gained a deeper understanding of the various types of grammars and how they relate to automata. We have also learned about the differences between NFA and DFA, and how they can be used to model different types of languages.

Furthermore, this laboratory work has demonstrated the importance of computational models in various fields, including computer science, linguistics, and artificial intelligence. The use of finite automata and related concepts has allowed us to describe and analyze language structures in a rigorous and systematic way.



