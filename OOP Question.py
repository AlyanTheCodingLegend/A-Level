import pickle
import datetime

# User Authentication
def authenticate_user():
    mainfile = open("Password file.DAT", "rb")
    user_id = input("Please enter your user ID: ")
    input_password = input("Please enter your password: ")
    address = hash(user_id)
    mainfile.seek(address)
    real_password = pickle.load(mainfile)
    if str(real_password) == str(input_password):
        return True
    else:
        print("Enter ID and Password again!")
        return False

# Product Management
class Product:
    def __init__(self, name, price, description):
        self.__name = name
        self.price = price
        self.quantity = 0
        self.__description = description

    def add_product(self):
        self.quantity += 1

    def remove_product(self):
        self.quantity -= 1

    def edit_amount(self, amount):
        self.quantity = amount

    def update_price(self, new_price):
        self.price = new_price

# Order Management
class Order:
    def __init__(self, customer_info):
        self.__date = datetime.date.today()
        self.__customer_info = customer_info
        self.__products = []

    def addproduct(self, product):
        self.__products.append(product)

    def cancel_order(self, product):
        self.__products.remove(product)

    def get_price(self):
        price = 0
        for product in self.__products:
            price += (product.quantity) * (product.price)
        return price

# Payment Method
class PaymentMethod:
    def __init__(self, method):
        self.method = method

    def process_payment(self, amount):
        print("Processing payment of", amount, "via", self.method)

# Inherited class for bank transfer payment method
class BankTransferPayment(PaymentMethod):
    def __init__(self):
        super().__init__("Bank Transfer")

    def process_payment(self, amount):
        print("Please transfer", amount, "to the provided bank account.")

# Inherited class for credit card payment method
class CreditCardPayment(PaymentMethod):
    def __init__(self):
        super().__init__("Credit Card")

    def process_payment(self, amount):
        print("Please enter your credit card details for payment.")

# Inherited class for PayPal payment method
class PayPalPayment(PaymentMethod):
    def __init__(self):
        super().__init__("PayPal")

    def process_payment(self, amount):
        print("Please log in to your PayPal account for payment.")

# Usage example
def main():
    if authenticate_user():
        laptop = Product("Laptop", 1000, "High-performance laptop")
        laptop.add_product()
        laptop.add_product()

        book = Product("Book", 20, "Interesting book")
        book.add_product()

        my_order = Order("Alyan Ahmed")
        my_order.addproduct(laptop)
        my_order.addproduct(book)

        print("Total Price: ", my_order.get_price())

        # Payment process
        payment_method = BankTransferPayment()  # Change payment method here
        payment_method.process_payment(my_order.get_price())


main()

    





















