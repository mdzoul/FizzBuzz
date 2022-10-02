from art import logo

logo()

user_input = int(input("Number:\n"))
max_value = user_input + 1

print(f"Initializing FizzBuzz Game for range 1 to {user_input}...")

for number in range(1, max_value):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
