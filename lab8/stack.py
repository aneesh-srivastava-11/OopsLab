class Stack:
    def __init__(self):
        self.size = 5
        self.stack = [None] * self.size
        self.top = -1
    def push(self, x):
        if self.top == self.size - 1:
            print("Stack Overflow!")
            return
        self.top += 1
        self.stack[self.top] = x
        print(f"Pushed {x}")
    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
            return
        val = self.stack[self.top]
        self.top -= 1
        print(f"Popped {val}")

    def peek(self):
        if self.top == -1:
            print("Stack Empty!")
            return
        print(f"Peek -> {self.stack[self.top]}")
    def display(self):
        if self.top == -1:
            print("Stack Empty!")
            return
        print("Stack (top -> bottom):", self.stack[self.top::-1])
def main():
    stack = Stack()
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            stack.push(int(input("Enter value: ")))
        elif ch == 2:
            stack.pop()
        elif ch == 3:
            stack.peek()
        elif ch == 4:
            stack.display()
        elif ch == 5:
            break
if __name__ == "__main__":
    main()
