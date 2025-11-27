def add(x, y):
    return x + y

def subtract(x , y):
    return x - y 

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("number is not divided by zero")
        return None
    return x / y

if __name__ == "__main__":
    print("testing math_ops")
    print(add(5, 6))
    print(subtract(10,5))


