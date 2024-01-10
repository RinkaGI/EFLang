from efConstants import *

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