class Order:
    def __init__ (self, order_id, customer_name, order_date, total_amount):
        self.order_id=order_id
        self.customer_name=customer_name
        self.order_date=order_date
        self.total_amount=total_amount
    def calculate_tax(self, total):
        return total * 0.1
    def display_order(self):
        print(f"ID: {self.order_id} | Nama: {self.customer_name} | Total: {self.total_amount}.")

class OrderProcessor:
    def __init__ (self):
        self.__order = []
    
    def add_order(self, item):
        self.__order.append(item)

    def calculate_total_revenue(self):
        self.total=0
        for x in self.__order:
            self.total += x.total_amount
    
    def calculate_total_tax(self):
        for x in self.__order:
            self.isi = x.calculate_tax(self.total)
        return self.isi

    def display_order(self):
        print(f"total belanja = {self.total} dan setelah diskon {self.isi}")

user1 = Order("3A231", "udin", "15-03-2026", 10_000)
user2 = Order("3A232", "ucok", "16-03-2026", 15_000)
user3 = Order("3A233", "joko", "17-03-2026", 5_000)

user1.display_order()
user2.display_order()
user3.display_order()

data = OrderProcessor()
data.add_order(user1)
data.add_order(user2)
data.add_order(user3)
data.calculate_total_revenue()
data.calculate_total_tax()
data.display_order()