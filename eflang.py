import sys, re

filepath = sys.argv[1]

PRINT_TOKEN = "PRINT_TOKEN"
STRING_TOKEN = "STRING_TOKEN"
NUMBER_TOKEN = "NUMBER_TOKEN"
BOOL_TRUE_TOKEN = "BOOL_TRUE_TOKEN"
BOOL_FALSE_TOKEN = "BOOL_FALSE_TOKEN"
NEWLINE_TOKEN = "NEWLINE_TOKEN"

PRINT_REGEX = "print "
STRING_REGEX = re.compile(r'"([^"]*)"')
NUMBER_REGEX = re.compile(r'[-+]?\b\d*\.?\d+\b')
BOOL_TRUE_REGEX = "true"
BOOL_FALSE_REGEX = "false"

NEWLINE_REGEX = "\n"

PRINT_COMMAND = "PRINT_COMMAND"

class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []
        self.line = 0

    def tokenize(self):
        lines = self.code.splitlines()

        for line in lines:
            self.line = self.line + 1
            
            if PRINT_REGEX in line:
                self.tokens.append({"name": "PRINT_TOKEN", "params": {}})
            
            match = STRING_REGEX.search(line)
            if match:
                self.tokens.append({"name": "STRING_TOKEN", "params": {"value": match.group(1)}})

            match = NUMBER_REGEX.search(line)
            if match:
                self.tokens.append({"name": "NUMBER_TOKEN", "params": {"value": match.group()}})

            if BOOL_TRUE_REGEX in line:
                self.tokens.append({"name": BOOL_TRUE_TOKEN, "params": {}})
            if BOOL_FALSE_REGEX in line:
                self.tokens.append({"name": BOOL_FALSE_TOKEN, "params": {}})

            if NEWLINE_REGEX in line:
                self.tokens.append({"name": NEWLINE_TOKEN, "params": {}})

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.parserResult = []
        self.line = 0
        self.tokenPos = -1

    def parse(self):
        for token in range(len(self.tokens) - 1):
            if self.tokens[token]["name"] == "PRINT_TOKEN":
                nextValue = self.tokens[token + 1]
                if nextValue["name"] == "STRING_TOKEN":
                    self.parserResult.append({"name": "PRINT_COMMAND", "params": {"value": str(nextValue["params"]["value"])}})
                elif nextValue["name"] == BOOL_TRUE_TOKEN:
                    self.parserResult.append({"name": "PRINT_COMMAND", "params": {"value": str(True)}})
                elif nextValue["name"] == BOOL_FALSE_TOKEN:
                    self.parserResult.append({"name": "PRINT_COMMAND", "params": {"value": False}})
                elif nextValue["name"] == NUMBER_TOKEN:
                    self.parserResult.append({"name": "PRINT_COMMAND", "params": {"value": str(nextValue["params"]["value"])}})

class Interpreter:
    def __init__(self, parsed):
        self.parsed = parsed

    def interpret(self):
        for token in self.parsed:
            if token["name"] == "PRINT_COMMAND":
                print(str(token["params"]["value"]))                   



f = open(filepath, "r")

lexer = Lexer(f.read())
lexer.tokenize()

parser = Parser(lexer.tokens)
parser.parse()

interpreter = Interpreter(parser.parserResult)
interpreter.interpret()