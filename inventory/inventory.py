class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity=1):
        self.items[name] = self.items.get(name, 0) + quantity

    def remove_item(self, name, quantity=1):
        if self.items.get(name, 0) < quantity:
            raise ValueError(f"Not enough {name} in stock")
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]


if __name__ == "__main__":
    stock = Inventory()
    stock.add_item("apple", 10)
    print(stock.items)
