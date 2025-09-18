class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at start")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at end")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at end")

    def insert_at_position(self, data, pos):
        if pos == 1:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                print("Position out of range!")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at position {pos}")

    def insert_at_middle(self, data):
        if not self.head:
            self.head = Node(data)
            print(f"Inserted {data} in middle")
            return
        slow, fast = self.head, self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_node = Node(data)
        new_node.next = slow.next
        slow.next = new_node
        print(f"Inserted {data} in middle")

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            print(f"Deleted {key}")
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Element not found!")
            return
        prev.next = temp.next
        print(f"Deleted {key}")

    def display(self):
        if not self.head:
            print("Linked List is Empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def main():
    ll = SinglyLinkedList()
    while True:
        print("\n--- Linked List Menu ---")
        print("1. Insert at Start")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Insert at Middle")
        print("5. Delete Node")
        print("6. Display")
        print("7. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            ll.insert_at_start(int(input("Enter value: ")))
        elif ch == 2:
            ll.insert_at_end(int(input("Enter value: ")))
        elif ch == 3:
            val = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            ll.insert_at_position(val, pos)
        elif ch == 4:
            ll.insert_at_middle(int(input("Enter value: ")))
        elif ch == 5:
            ll.delete(int(input("Enter value to delete: ")))
        elif ch == 6:
            ll.display()
        elif ch == 7:
            break

if __name__ == "__main__":
    main()
