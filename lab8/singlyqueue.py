class Queue:
    def __init__(self):
        self.size = 5
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if self.rear == self.size - 1:
            print("Queue Overflow!")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = x
        print(f"Enqueued {x}")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow!")
            return
        val = self.queue[self.front]
        self.front += 1
        print(f"Dequeued {val}")

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Empty!")
            return
        print("Queue (front -> rear):", self.queue[self.front:self.rear + 1])


def main():
    q = Queue()
    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            q.enqueue(int(input("Enter value: ")))
        elif ch == 2:
            q.dequeue()
        elif ch == 3:
            q.display()
        elif ch == 4:
            break

if __name__ == "__main__":
    main()
