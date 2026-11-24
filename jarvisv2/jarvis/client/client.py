class Message:
    def __init__(self, message):
        self.message = message

    def contains(self, word, case_sensitive=False):
        if case_sensitive:
            return word in self.message
        return word.lower() in self.message.lower()
