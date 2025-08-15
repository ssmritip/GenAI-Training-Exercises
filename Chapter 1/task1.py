import json
from abc import ABC, abstractmethod
from pathlib import Path


class Store(ABC):
    @abstractmethod
    def purchase_item(self, user_cred, item_name):
        pass

    @abstractmethod
    def store_item(self, item_name, item_count, department):
        pass


class Groceries(Store):
    def __init__(self, file):
        super().__init__()
        self.file = Path(file)
        if not self.file.exists():
            # initialize with empty list
            with open(self.file, "w") as f:
                json.dump([], f, indent=4)

    def _load_items(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def _save_items(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def purchase_item(self, user_cred, item_name):
        data = self._load_items()
        for item in data:
            if item["item"] == item_name:
                if item["count"] > 0:
                    item["count"] -= 1
                    self._save_items(data)
                    print(f"Customer: {user_cred['Name']} (ID: {user_cred['UserId']})")
                    print(f"Purchased: {item_name}")
                else:
                    print(f"Sorry, {item_name} is out of stock.")
                return
        print(f"{item_name} not found in store.")

    def store_item(self, item_name, item_count, department):
        data = self._load_items()
        for item in data:
            if item["item"] == item_name and item["department"] == department:
                item["count"] += item_count
                self._save_items(data)
                break
        else:
            # Add new item if not found
            data.append({
                "department": department,
                "item": item_name,
                "count": item_count
            })
            self._save_items(data)

        print("\nCurrent Store Inventory:")
        for item in data:
            print(f"- {item['department']}: {item['item']} - {item['count']} available")

    def inspect(self):
        data = self._load_items()
        print("=== Store Inventory ===")
        for item in data:
            print(f"{item['department']}: {item['item']} - {item['count']} in stock")

class Electronics(Store):
    def __init__(self, file):
        super().__init__()
        self.file = Path(file)
        if not self.file.exists():
            with open(self.file, "w") as f:
                json.dump([], f, indent=4)

    def _load_items(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def _save_items(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def purchase_item(self, user_cred, item_name):
        data = self._load_items()
        for item in data:
            if item["item"] == item_name and item["department"] == "Electronics":
                if item["count"] > 0:
                    item["count"] -= 1
                    self._save_items(data)
                    print(f"Customer: {user_cred['Name']} (ID: {user_cred['UserId']})")
                    print(f"Purchased: {item_name}")
                else:
                    print(f"Sorry, {item_name} is out of stock.")
                return
        print(f"{item_name} not found in Electronics department.")

    def store_item(self, item_name, item_count, department="Electronics"):
        data = self._load_items()
        for item in data:
            if item["item"] == item_name and item["department"] == department:
                item["count"] += item_count
                self._save_items(data)
                break
        else:
            data.append({
                "department": department,
                "item": item_name,
                "count": item_count
            })
            self._save_items(data)

        print("\nCurrent Electronics Inventory:")
        for item in data:
            if item["department"] == "Electronics":
                print(f"- {item['item']} - {item['count']} available")

if __name__ == "__main__":
    user1 = {
        "UserId": "0041",
        "Name": "Sam Rai"
    }

    grocery = Groceries("file.json")
    grocery.inspect()
    grocery.store_item("Apples", 5, "Produce")
    grocery.store_item("Bananas", 3, "Produce")
    grocery.purchase_item(user1, "Apples")

    electronics = Electronics("file.json")
    electronics.store_item("Headphones", 2)
    electronics.store_item("Laptop", 1)
    electronics.purchase_item(user1, "Laptop")
