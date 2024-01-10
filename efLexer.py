from efConstants import *

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
