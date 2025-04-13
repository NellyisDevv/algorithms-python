import time

# --- Node and LinkedList implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """Add value to the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_middle(self, index, value):
        """Insert value at a specific index."""
        if index <= 0:
            self.prepend(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                break
            current = current.next
        new_node.next = current.next if current else None
        if current:
            current.next = new_node

    def get(self, index):
        """Get value at a specific index."""
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.value if current else None

    def delete(self, index):
        """Delete the node at a specific index."""
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

# --- Benchmarking Functions ---

def time_operation(operation, data_structure, n):
    start_time = time.time()
    operation(data_structure, n)
    return time.time() - start_time

def test_append(ds, n):
    for i in range(n):
        ds.append(i)

def test_prepend(ds, n):
    for i in range(n):
        ds.prepend(i)

def test_insert_middle(ds, n):
    for i in range(n):
        ds.insert_middle(i // 2, i)

def test_random_access(ds, n):
    for i in range(n):
        _ = ds.get(i // 2)

def test_delete(ds, n):
    for i in range(n):
        ds.delete(0)

# --- Run and Compare Tests ---

def run_experiment(n=10000):
    tests = {
        "Append": test_append,
        "Prepend": test_prepend,
        "Insert in Middle": test_insert_middle,
        "Random Access": test_random_access,
        "Delete from Beginning": test_delete
    }

    for test_name, test_func in tests.items():
        print(f"\n--- {test_name} Test ---")

        # Test Python list
        py_list = []
        py_time = time_operation(test_func, py_list, n)
        print(f"Python list time:     {py_time:.4f} seconds")

        # Test custom linked list
        linked_list = LinkedList()
        ll_time = time_operation(test_func, linked_list, n)
        print(f"Linked list time:     {ll_time:.4f} seconds")

if __name__ == "__main__":
    run_experiment()
