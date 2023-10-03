# https://adventofcode.com/2020/day/2
# Validate passwords from a list based on the conditions given with each password.
# Example: 3-4 j: tjjj
# Password must contain between 3 and 4 "j"s, password listed after colon.

# data_path =("example2.txt")
data_path = ("day2.txt")

with open(data_path, "r") as input_file:
    correct_passwords = 0

    """ Part 2  - Each policy actually describes two positions in the password,
     where 1 means the first character, 2 means the second character, and so on. 
     (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
     Exactly one of these positions must contain the given letter. Other occurrences 
     of the letter are irrelevant for the purposes of policy enforcement.
     """
    # correct_passwords = 0

    for line in input_file:
        line = line.replace(": ", " ").replace("-", " ")    # Converts gaps between data to spaces
        line = line.split(" ")  # Splits string into a list of the data in string form
        # print(line) # expect['int', 'int, 'character str', 'password str'

        min_times = int(line[0])
        max_times = int(line[1])
        target_char = line[2]
        password = line[3]
        count = password.count(target_char)



        # if min_times <= count <= max_times:
        if password[min_times] == target_char or  password[max_times] == target_char:
            correct_passwords += 1

    print(f"part 2 correct_passwords =", correct_passwords)
    # example data result = 2 CORRECT
    # day-2 data result = 690 CORRECT
