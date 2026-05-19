class Countdown:
    """
    Implementation of the Iterator Protocol.
    """
    def __init__(self, start: int):
        self.items = [num for num in range(1, start)]
        self.index = len(self.items)

    def __post_init__(self):
        self.items.sort(reverse=True)


    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        current_element = self.items[self.index - 1]
        self.index -= 1
        return current_element
