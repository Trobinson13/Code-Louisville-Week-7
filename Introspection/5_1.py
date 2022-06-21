from itertools import chain

def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

class Batch:
    def __init__(self, iterables=()):
        self._iterables = list(iterables)

    def append(self, iterable):
        self._iterables.append(iterable)

    def __iter__(self):
        return chain(*self._iterables)

print(f":\n{int}\n")