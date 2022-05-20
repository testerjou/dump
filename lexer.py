class Lexer: 
    def __init__(self, input) -> None:
        self.input = input.lower()
        pass
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'
    LETTERS = 'abcdefghjiklmnopqrstuvxyzåöä'

    def get_next(self):
        pass
    def create_tokens(self):

        token_list = []
        current_word = ""
        current_char = ""

        #i = index, v = value
        for i, v in enumerate(input):
            #if i + 1 == len(input):
            #    break
            
            if v in self.LETTERS:
                current_word += v

            if v.isspace():
                print("Works", " value ", v, "123")
                #checkword
                print(current_word)
                current_word = ""
            
            pass

        for i in range(len(input)):
            pass
        

        pass

input = "Eteen 5 Taakse 5"
lex = Lexer(input)
print(lex.input)
print("Hello")

lex.create_tokens()