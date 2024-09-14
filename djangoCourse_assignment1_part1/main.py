# assignment 1
# part 1: decorator log

def log_decorator(func):
    def wrapper(*args):
        print(f'Calling function: {func.__name__}')
        print(f'Arguments: args={args}')
        print(f'Function {func.__name__} returned {func(*args)}')
    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def greet(name, greeting):
    return f'{greeting}, {name}!'


@log_decorator
def factorial(n):
    output = 1
    for num in range(2, n+1):
        output *= num
    return output


lines = []

for i in range(3):  # getting three lines from the user
    line = input()
    lines.append(line)

first_input = lines[0].split()
add(int(first_input[0]), int(first_input[1]))

second_input = lines[1].split()
greet(second_input[0], second_input[1])

factorial(int(lines[2]))
