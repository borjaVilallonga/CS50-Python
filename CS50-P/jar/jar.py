class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Negative cookies not allow")

        self.n = 0
        self._capacity = capacity

    def __str__(self):
        return "🍪" * self.n

    def deposit(self, n):
        if self.n + n > self.capacity:
            raise ValueError("Too much cookies")
        self.n += n

    def withdraw(self, n):
        if self.n < n:
            raise ValueError("Not enough cookies")
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n
