"""AoC 1, 2020: Report Repair"""

# Standard library imports
ç

def parse(puzzle_input):
    """Parse input"""
    numbers = [int(line) for line in puzzle_input.split()]
    # return [int(line) for line in puzzle_input.split()]

def part1(numbers):
    """Solve part 1"""
    for num1 in numbers:
        for num2 in numbers:
            print(num1, num2)
            if num1 < num2 and num1 + num2 == 2020:
                print("part 1 = ", (num1 * num2))
                # return num1 * num2


def part2(numbers):
    """Solve part 2"""

    ############## Day 1: Challenge B ##############
    f = open('data/day1.data')

    make_me_new_data = []
    for line in f:
        make_me_new_data.append(int(line))

    sliding_window_measure = 3
    indexes_to_try = len(make_me_new_data) - sliding_window_measure
    incrementer = 0
    for index_ in range(indexes_to_try):
        a = make_me_new_data[index_] + make_me_new_data[index_ + 1] + make_me_new_data[index_ + 2]
        b = make_me_new_data[index_ + 1] + make_me_new_data[index_ + 2] + make_me_new_data[index_ + 3]
        if b > a:
            incrementer += 1

    print(incrementer)

    # Answer = 1457


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    #solution2 = part2(data)

    return solution1, # solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
