class Lexer: 
    def __init__(self, input) -> None:

        self.input = input.lower()

        pass
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'
    LETTERS = 'abcdefghjiklmnopqrstuvxyzåöä'


print("Hello")