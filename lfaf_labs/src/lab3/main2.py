from lexer import Lexer
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

lexer = Lexer(text)
tokens = lexer.lex()

for token in tokens:
    print(token)