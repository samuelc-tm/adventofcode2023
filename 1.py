f = open("1.txt", "r")

total = 0
for line in f:
    number = []
    for char in line:
        if char.isdigit():
            number.append(char)
    double_digit_number = number[0] + number[-1]
    total += int(double_digit_number)
    
print(total)