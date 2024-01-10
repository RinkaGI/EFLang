class Interpreter:
    def __init__(self, parsed):
        self.parsed = parsed

    def interpret(self):
        for token in self.parsed:
            if token["name"] == "PRINT_COMMAND":
                print(str(token["params"]["value"]))    