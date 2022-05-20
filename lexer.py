class Lexer: 
    def __init__(self, input) -> None:
        self.input = input.lower()
        pass
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'
    LETTERS = 'abcdefghjiklmnopqrstuvxyzåöä'

    def advance():
        current_word = ""
        current_char = ""

input = "Eteen 5 Taakse 5"
lex = Lexer(input)
print(lex.input)
print("Hello")