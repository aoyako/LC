class ProductOfNumbers:

    def __init__(self):
        self.cache = []
        self.last_call = None

    def add(self, num: int) -> None:
        self.cache.append(num)
        self.last_call = None

    def getProduct(self, k: int) -> int:
        if self.last_call:
            args, val = self.last_call
            if args == k:
                return val
        res = 1
        for x in self.cache[-k:]:
            res *= x
        self.last_call = (k, res)
        return res


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)