import sys

def main():
    jar = Jar()

    jar.deposit(8)

    print(jar)

class Jar:
    def __init__(self, capacity=12, size=0):
        try:
            self.capacity = capacity
            
            if self.capacity < 0:
                raise ValueError()
        except (ValueError):
            sys.exit("\nCapacity must be a positive number")

        self.size = size

    def __str__(self):
        print()
        return f"🍪" * self.size

    def deposit(self, n):
        try:
            self.size = self.size + n
        
            if self.size > self.capacity:
                raise ValueError()
        except ValueError:
            sys.exit("\nJar capacity exceeded")
        else:
            return self.size

    def withdraw(self, n):
        try:
            self.size = self.size - n
        
            if n > self.size:
                raise ValueError()
        except ValueError:
            sys.exit("\nNot enough cookies in jar to remove")
        else:
            return self.size

    def capacity(self):
        return self.capacity

    def size(self):
        return self.size
        
if __name__ == "__main__":
    main()