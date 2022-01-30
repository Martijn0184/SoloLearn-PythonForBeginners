#Any code placed after the return statement won't be executed.
def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 2))