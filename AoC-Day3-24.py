import re

with open('inputs/input03.txt') as i:
    memoryInput = i.read()

def find_mul(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, input)

def find_mul_do_dont(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    return re.findall(pattern, input)

def mul(value):
    _, numbers = value.split("(", 1)
    numbers = numbers[:-1]  # remove the closing parenthesis
    left, right = numbers.split(",")
    return int(left) * int(right)

def main():
    part_a = sum(mul(m) for m in find_mul(memoryInput))   
    part_b = 0
    do = True
    for m in find_mul_do_dont(memoryInput):
        if m == "do()": do = True
        elif m == "don't()": do = False
        elif m.startswith("mul") and do: part_b += mul(m)
    print("A: ", part_a)
    print("B: ", part_b)

main()