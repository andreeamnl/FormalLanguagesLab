# Lexer & Scanner

### Course: Formal Languages & Finite Automata
### Author: Andreea Manole

----

## Objectives:
1. Understand what lexical analysis [1] is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.


## Implementation description

* I use two classes, ```Token``` and ```Lexer```. Token uses a keyword dictionary to be used by the lexer in order to identify them in the code input. The lexer class has a 'lex' function to iterate through each input charachter, identify it's type and return it to the user.
```
        while self.pos < len(self.text):
            if self.text[self.pos].isdigit():  
                st=""
                while(self.text[i].isdigit()):
                    st+=self.text[i]
                    i+=1
                self.pos=i
                tokens.append(Token('INTEGER', int(st)))
```



* The code you see above is used to identify digit literals, we loop through chars until we no longer see ints, the merged string is returned to the user.


```
            if self.text[self.pos].isalpha():  
                i=self.pos
                st=""
                while(self.text[i].isalpha()):
                    st+=self.text[i]
                    i+=1
                self.pos=i
                if(st in Token.keywords):
                    tokens.append(Token(f'{Token.keywords[st]}', st))
                else:
                    tokens.append(Token('IDENT', st))
```

* The code above is used to return identifiers, again we loop through the string, if it appears in ```token.keywords``` we return it as such, otherwise we return it as a plain identifier.

```
            elif self.text[self.pos] == '+':
                tokens.append(Token('PLUS', '+'))
                self.advance()
            elif self.text[self.pos] == '-':
                tokens.append(Token('MINUS', '-'))
                self.advance()
            elif self.text[self.pos] == '=':
                tokens.append(Token('EQUAL', '='))
                self.advance()
```
* The code above is part of the symbol identification process.

```
            elif self.text[self.pos] == '#':
                i=self.pos
                st=""
                while(self.text[i]!='\n'):
                    st+=self.text[i]
                    i+=1
                self.pos=i
                tokens.append(Token('COMMENT', st))
                self.advance()
```
* Here we merge comment words, we only stop when we encounter '\n'


## Results

* Here is the input code I used.
```
text = '''def bubblesort(arr):
    n = len(arr)
    # Traverse through all array elements\n
    for i in range(n):
        # Last i elements are already sorted\n
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element\n
            #nota 10 pls ^_^\n
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
'''
```

* Here is the output 
```
Token(FUNCTION, def)
Token(IDENT, bubblesort)
Token(LPAREN, ()
Token(IDENT, arr)
Token(RPAREN, ))
Token(COLON, :)
Token(IDENT, n)
Token(EQUAL, =)
Token(LEN, len)
Token(LPAREN, ()
Token(IDENT, arr)
Token(RPAREN, ))
Token(COMMENT, # Traverse through all array elements)
Token(FOR, for)
Token(IDENT, i)
Token(IN, in)
Token(RANGE, range)
Token(LPAREN, ()
Token(IDENT, n)
Token(RPAREN, ))
Token(COLON, :)
Token(COMMENT, # Last i elements are already sorted)
Token(FOR, for)
Token(IDENT, j)
Token(IN, in)
Token(RANGE, range)
Token(LPAREN, ()
Token(INTEGER, 0)
Token(COMMA, ,)
Token(IDENT, n)
Token(MINUS, -)
Token(IDENT, i)
Token(MINUS, -)
Token(INTEGER, 1)
Token(RPAREN, ))
Token(COLON, :)
Token(COMMENT, # Swap if the element found is greater than the next element)
Token(COMMENT, #nota 10 pls ^_^)
Token(IF, if)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(RBRACKET, ])
Token(GREATER, >)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(PLUS, +)
Token(INTEGER, 1)
Token(RBRACKET, ])
Token(COLON, :)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(RBRACKET, ])
Token(COMMA, ,)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(PLUS, +)
Token(INTEGER, 1)
Token(RBRACKET, ])
Token(EQUAL, =)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(PLUS, +)
Token(INTEGER, 1)
Token(RBRACKET, ])
Token(COMMA, ,)
Token(IDENT, arr)
Token(LBRACKET, [)
Token(IDENT, j)
Token(RBRACKET, ])
```
## Conclusions 

* In conclusion, programming a lexer is a crucial skill for anyone interested in developing programming languages, compilers, or interpreters. Throughout this laboratory work, I learned how to identify and tokenize various types of tokens, such as keywords, identifiers, numbers, and operators. I also gained experience in implementing a lexer and testing it with different inputs to ensure its accuracy and efficiency.

* Moreover, I realized that the lexer is a critical component in the overall process of interpreting or compiling code. It serves as the building block for other parts of the interpreter or compiler and must be efficient and dependable.

* Overall, this laboratory work has provided me with valuable knowledge and skills that will be useful in building more complex interpreters and compilers in the future.


## References

* LLVM. (n.d.). Chapter 1 - Building a language frontend. LLVM Tutorial. Retrieved March 25, 2023, from https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html
