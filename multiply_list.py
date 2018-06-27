numbers = [1, 2, 3, 4, 5, 6]
prompt = int(raw_input("Pick a number: "))

new_numbers = []

for number in numbers:
    new_number = number * prompt
    new_numbers.append(new_number)
print new_numbers
