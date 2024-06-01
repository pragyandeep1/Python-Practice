import pickle

class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            self.file = None
        self.lineno = 0

    def readline(self):
        if self.file is None:
            return None
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        if self.filename is not None:  # Check if filename is not None
            try:
                self.file = open(self.filename)
                for _ in range(self.lineno):
                    self.file.readline()
            except FileNotFoundError:
                print(f"File '{self.filename}' not found.")
                self.file = None
        else:
            self.file = None

reader = TextReader("Geeksforgeeks.txt")
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())
