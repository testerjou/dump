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

        print("Input",self.input)
        split_list = input.split()

        for element in split_list:
            if element in self.KEYWORDS:
                token_list.append(("KEYWORD",element))
            elif element in self.DIGITS:
                token_list.append(("INT", element))
            else:
                print("NOT FOUND ", element)
        print("TOKENS:",token_list)


    def create_tokens1(self):

        token_list = []
        current_word = ""
        current_char = ""

        #i = index, v = value

        print("Input",self.input)

        split_list = input.split()

        print("split_list", split_list)

        for i, v in enumerate(self.input):
            #if i + 1 == len(input):
            #    break
            
            if v in self.LETTERS:
                current_word += v

            if v in self.DIGITS:
                current_char = v 

            if v.isspace():
                #checkword
                print(current_word)
                

                if current_word in self.KEYWORDS:
                    token_list.append(("KEYWORD",current_word))
                if current_char in self.DIGITS:
                    token_list.append(("INT", current_char))
                current_word = ""
                current_char = ""
            pass

        print(token_list)

        for i in range(len(input)):
            pass
        

        pass

input = "Eteen 5 Taakse 5"
lex = Lexer(input)

lex.create_tokens()