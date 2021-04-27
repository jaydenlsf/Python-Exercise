def print_lines(filename, mode, index1, index2):
    file = open(filename, mode)
    lines = file.read().splitlines()
    specific_lines = lines[index1], lines[index2]

    return specific_lines


print(print_lines("teams.txt", "r", 0, 3))
