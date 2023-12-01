import re

f = open("1.txt", "r")

text_int_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0
for line in f:    
    matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    print(matches)
    number0 = matches[0]
    number1 = matches[-1]
    if number0 in list(text_int_map.keys()):
        number0 = text_int_map[number0]
    if number1 in list(text_int_map.keys()):
        number1 = text_int_map[number1]
    double_digit_number = str(number0) + str(number1)
    print(double_digit_number)
    total += int(double_digit_number)
    
print(total)