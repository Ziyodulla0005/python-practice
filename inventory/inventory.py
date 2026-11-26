class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity=1):
        self.items[name] = self.items.get(name, 0) + quantity


if __name__ == "__main__":
    stock = Inventory()
    stock.add_item("apple", 10)
    print(stock.items)
