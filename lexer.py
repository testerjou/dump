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

        print("Input",self.input)

        for i, v in enumerate(self.input):
            #if i + 1 == len(input):
            #    break
            
            if v in self.LETTERS:
                print(i)
                current_word += v
                print(i)
            if v.isspace():
                #checkword
                print(current_word)
                current_word = ""
                
                if current_word in self.KEYWORDS:
                    token_list.append((current_word,))
            
            pass

        print(token_list)

        for i in range(len(input)):
            pass
        

        pass

input = "Eteen 5 Taakse 5"
lex = Lexer(input)

lex.create_tokens()