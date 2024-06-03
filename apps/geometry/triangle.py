class Triangle:

    def __init__(self, base, height, length):
        if length >= base + height or base >= length + height or height >= base + length:
            raise ValueError("Invalid side lengths")
        self.base = base
        self.height = height
        self.length = length

    def is_right_triangle(self):
        return self.base ** 2 + self.height ** 2 == self.length ** 2

    def get_perimeter(self):
        return self.base + self.height + self.length

    def get_area(self):
        if self.is_right_triangle():
            return 0.5 * self.base * self.height
        else:
            s = (self.base + self.height + self.length) / 2
            return (s * (s - self.base) * (s - self.height) * (s - self.length)) ** 0.5
