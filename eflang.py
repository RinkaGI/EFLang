import sys, re
from efLexer import Lexer
from efParser import Parser
from efInterpreter import Interpreter


# getting code
filepath = sys.argv[1]
f = open(filepath, "r")

# tokenize all code
lexer = Lexer(f.read())
lexer.tokenize()

# parsing all code
parser = Parser(lexer.tokens)
parser.parse()

# run the code
interpreter = Interpreter(parser.parserResult)
interpreter.interpret()