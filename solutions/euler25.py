

def fib():
    prev = 1
    current = 1
    index = 3
    while len(str(current)) < 1000:
        prev, current = current, prev + current
        index += 1
    print(f"{index-1}: {len(str(current))}")


fib()