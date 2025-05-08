class Calculator:
    """
    A simple calculator that can perform:
      - Addition
      - Subtraction
      - Multiplication
      - Division
      - Taking the nth root
      - Resetting memory to 0
    """

    def __init__(self):
        """Initialize calculator with memory set to 0."""
        self.memory = 0.0

    def add(self, value):
        """Add a number to memory."""
        self.memory += value
        return self.memory

    def subtract(self, value):
        """Subtract a number from memory."""
        self.memory -= value
        return self.memory

    def multiply(self, value):
        """Multiply memory by a number."""
        self.memory *= value
        return self.memory

    def divide(self, value):
        """Divide memory by a number. Raises error if dividing by zero."""
        if value == 0:
            raise ValueError("Cannot divide by zero.")
        self.memory /= value
        return self.memory

    def nth_root(self, n):
        """Take the nth root of the memory. Raises error if root is invalid."""
        if n == 0:
            raise ValueError("Cannot take the zeroth root.")
        if self.memory < 0 and n % 2 == 0:
            raise ValueError("Cannot take an even root of a negative number.")
        self.memory = self.memory ** (1 / n)
        return self.memory

    def reset(self):
        """Reset memory to 0."""
        self.memory = 0.0
