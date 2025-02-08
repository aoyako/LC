class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.indexes = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.numbers:
            prev = self.numbers[index]
            self.indexes[prev].remove(index)
        self.numbers[index] = number
        self.indexes[number].add(index)
        

    def find(self, number: int) -> int:
        if len(self.indexes[number]) == 0:
            return -1
        return self.indexes[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)