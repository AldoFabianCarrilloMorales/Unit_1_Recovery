#Lab 4: Object Aggregation & State Management
from typing import List

class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = float(price)
        self.category = category.lower()

    def get_tax_rate(self) -> float:
        return self.TAX_RATES.get(self.category, 0.0)

    def calculate_final_price(self) -> float:
        tax_rate = self.get_tax_rate()
        return self.price * (1.0 + tax_rate)

    TAX_RATES = {
            "electronics": 0.16,
            "clothes": 0.08,
            "food": 0.00
        }

class Order:
    def __init__(self, order_number: int, customer_name: str):
        self.order_number = order_number
        self.customer_name = customer_name
        self.products: List[Product] = []
        self.status = "Created"

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        print(f"[Order #{self.order_number}] Product added: '{product.name}' (${product.price:.2f})")

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.products:
            total += item.calculate_final_price()
        return total

    def change_status(self, new_status: str) -> None:
        previous_status = self.status
        self.status = new_status.upper()
        print(f"Order #{self.order_number} changed from '{previous_status}' to '{self.status}'.")

    def show_order(self) -> None:
        print(f" ORDER SUMMARY #{self.order_number}")
        print(f" Customer: {self.customer_name}")
        print(f" Status:   {self.status}")
        print(f" {'product':<25} {'Category':<15} {'Base Price':<12} {'TOTAL WITH TAX'}")


        base_subtotal = 0.0
        for item in self.products:
            final_price = item.calculate_final_price()
            base_subtotal += item.price
            tax_pct = int(item.get_tax_rate() * 100)
            print(f" {item.name:<25} {item.category.capitalize():<15} ${item.price:<11.2f} ${final_price:.2f} ({tax_pct}% Tax)")

        grand_total = self.calculate_total()
        total_taxes = grand_total - base_subtotal

        print(f" Base Subtotal:  ${base_subtotal:.2f}")
        print(f" Total Taxes:    ${total_taxes:.2f}")
        print(f" GRAND TOTAL:    ${grand_total:.2f}")

# TESTING GROUNDS

if __name__ == "__main__":
    # 1.- Order Initialization
    order1 = Order(order_number=1001, customer_name="Aldo Carrillo")

    # 2.- Product Aggregation
    prod1 = Product(name="OLED Smartphone", price=12000.00, category="electronics")
    prod2 = Product(name="sweater", price=850.00, category="clothes")
    prod3 = Product(name="Fruit Basket", price=350.00, category="food")

    order1.add_product(prod1)
    order1.add_product(prod2)
    order1.add_product(prod3)

    # 3.- Summary % calculations
    order1.show_order()

    # 4.- State Transition
    order1.change_status("Porcessing")
    order1.change_status("Shipped")

    order1.show_order()