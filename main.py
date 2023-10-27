# Problem 715.
# Range Module.

class RangeModule:

    def __init__(self):
        self.numbers = []

    def addRange(self, left: int, right: int) -> None:
        for number in range(left, right):
            if number not in self.numbers:
                self.numbers.append(number)

    def queryRange(self, left: int, right: int) -> bool:
        for number in range(left, right):
            if number not in self.numbers:
                return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        for number in range(left, right):
            if number in self.numbers:
                self.numbers.remove(number)


if __name__ == '__main__':

