class Book:
    def __init__(self, **kwargs):
        self.bookname = kwargs.get("name", "Unknown")
        self.price = kwargs.get("price", 0)

    def __add__(self, other):
        return Book(name= "Total " ,price=self.price + other.price)

    def __sub__(self, other):
        return self.price - other.price

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price

    def __floordiv__(self, other):
        return self.price // other.price

    def __mod__(self, other):
        return self.price % other.price

    def __eq__(self, other):
        return self.price == other.price

    def __str__(self):
        return f"{self.bookname} - ₹{self.price}"

# Creating book objects using keyword arguments
b1 = Book(name="Core Python", price=200)
b2 = Book(name="Advance Python", price=400)
b3 = Book(name="Tricks Python", price=300)
b4 = Book(name="Master Python", price=500)

# Demonstration of operations
print("Add:", b1 + b2 + b3 + b4)    # Works now!
print("Sub:", b2 - b1)
print("Mul:", b1 * b2)
print("Div:", b2 / b1)
print("Floor Div:", b2 // b1)
print("Mod:", b2 % b1)
print("Equal:", b1 == b2)
