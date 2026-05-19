class Countdown:
    """
    Implementation of the Iterator Protocol.
    """

    def __init__(self, start: int):
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        value = self.current
        self.current -= 1
        return value
