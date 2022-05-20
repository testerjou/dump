class Lexer: 
    def __init__(self, input):
        self.input = input.lower()
        pass
    
    KEYWORDS = ['eteen', 'taakse', 'oikealle', 'vasemmalle']
    DIGITS = '0123456789'

    def get_next(self):
        pass

    def create_tokens(self):
        token_list = []

        print("Input",self.input)
        split_list = [element.lower() for element in input.split()]
        print("Split:",split_list)
        for element in split_list:
            if element in self.KEYWORDS:
                token_list.append(("KEYWORD",element))
            elif element in self.DIGITS:
                token_list.append(("INT", element))
            else:
                print("NOT FOUND ", element)
        print("TOKENS:",token_list)

    def set_input(self, input):
        self.input = input

input = "Eteen 5 Taakse 5"
lex = Lexer(input)
lex.create_tokens()

lex.set_input("Eteen5 Taakse5")
lex.create_tokens()

lex.set_input("Eteen5Taakse5")
lex.create_tokens()
