prompt = int(raw_input("Pick a number: "))

for number in range(1, (prompt + 1)):
    if number % 2 == 0:
        print number
    else:
        pass