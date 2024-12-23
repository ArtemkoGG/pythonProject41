def is_file_numbers_only(file_0):
    with open(file_0, "r") as file:
        return all(line.isdigit() for line in file)

print(is_file_numbers_only("input.txt"))
