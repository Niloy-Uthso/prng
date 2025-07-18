

import matplotlib.pyplot as plt

class SimpleLCG:
    def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m  # Normalize to [0,1]

    def generate(self, n):
        return [self.next() for _ in range(n)]

if __name__ == "__main__":
    prng = SimpleLCG(seed=42)
    numbers = prng.generate(1000)

    plt.hist(numbers, bins=20, edgecolor='black')
    plt.title("PRNG Output Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

    # Optional: Scatter plot for dependency check
    plt.scatter(numbers[:-1], numbers[1:], alpha=0.5)
    plt.title("PRNG Dependency Plot (Xn vs Xn+1)")
    plt.xlabel("Xn")
    plt.ylabel("Xn+1")
    plt.show()
