# unordered lists

class UnorderedList:
    def __init__(self):
        self.items = []  # Start with an empty list

    def add(self, item):
        self.items.append(item)  # Add an item to the end of the list

    def remove(self, item):
        if item in self.items:  # Check if the item exists
            self.items.remove(item)  # Remove the item

    def search(self, item):
        return item in self.items  # Check if the item is in the list

    def size(self):
        return len(self.items)  # Return the number of items in the list

    def is_empty(self):
        return len(self.items) == 0  # Check if the list is empty


# Example usage
unordered_list = UnorderedList()
unordered_list.add("apple")
unordered_list.add("banana")
unordered_list.add("cherry")

print("List size:", unordered_list.size())  # Output: List size: 3
print("Is 'banana' in the list?", unordered_list.search("banana"))  # Output: True

unordered_list.remove("banana")
print("Is 'banana' in the list after removal?", unordered_list.search("banana"))  # Output: False
print("List size after removal:", unordered_list.size())  # Output: List size: 2

