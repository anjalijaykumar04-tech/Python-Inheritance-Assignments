class Product:
    def display(self):
        print("Product: Laptop")
        print("Price: 50000")

class Discount(Product):
    def calculate(self, price, discount):
        final_price = price - (price * discount / 100)
        print("Final Price:", final_price)

d = Discount()
d.display()
d.calculate(50000, 10)