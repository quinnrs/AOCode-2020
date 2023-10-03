# https://adventofcode.com/2020/day/2
# Validate passwords from a list based on the conditions given with each password.
# Example: 3-4 j: tjjj
# Password must contain between 3 and 4 "j"s, password listed after colon.

# data_path =("example2.txt")
data_path = ("day2.txt")

with open(data_path, "r") as input_file:
    correct_passwords = 0

    for line in input_file:
        line = line.replace(": ", " ").replace("-", " ")    # Converts gaps between data to spaces
        line = line.split(" ")  # Splits string into a list of the data in string form
        # print(line) # expect['int', 'int, 'character str', 'password str'

        min_times = int(line[0])
        max_times = int(line[1])
        target_char = line[2]
        password = line[3]
        count = password.count(target_char)

        if min_times <= count <= max_times:
            correct_passwords += 1

    print(f"part 1 correct_passwords =", correct_passwords)
    # example data result = 1 CORRECT
    # day-2 data result = 393 CORRECT

