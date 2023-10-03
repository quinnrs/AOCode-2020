import pathlib
import sys

# https://adventofcode.com/2020/day/1
# Correct error in expense report by finding entries that sumt  o 2020.
# Example entries = [1721, 979, 366, 299, 575, 1456]

#  data_path = "example1.txt"
data_path =("day_1.txt")

numbers = []
f = open(data_path)
numbers += [int(line) for line in f]
print(numbers)

# from aocd.models import Puzzle
# puzzle = Puzzle(year=2020, day=1)
# puzzle.input_data[:20]

# def parse(data_path):
#     """Parse input"""

# call the function
# parse(data_path)

# numbers = [1721, 979, 366, 299, 575, 1456]

def part1(numbers):
    """Solve part 1"""
    for num1 in numbers:
        for num2 in numbers:
            # print(num1, num2)
            if num1 < num2 and num1 + num2 == 2020:
                print("part 1 = ", (num1 * num2))
                return num1 * num2

# call the function
# numbers = parse(data_path)
part1 = (print(f"part1 = ", part1(numbers)))
"""  example data = 514579   day_1 data = 913824   """

def part2(numbers):
    """Solve part 2 """
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                # print(num1, num2, num3)
                if num1 < num3 and num1 + num2 + num3 ==2020:
                    # if num1 + num2 + num3 == 2020:
                    print(num1, num2, num3)
                    print(f"sum = ", (num1 + num2 + num3))
                    print("part 2 = ", (num1 * num2 * num3))
                    return num1 * num2 * num3

# call the function
part2 = (print(f"part2 = ", part2(numbers)))
"""   example data = 241861950   day_1 data =  240889536   """