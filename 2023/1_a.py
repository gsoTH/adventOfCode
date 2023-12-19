# https://adventofcode.com/2023/day/1
#
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# In this example, the calibration values of these four lines are 12, 38, 15, and 77.
# Adding these together produces 142.

def read_input(is_test: bool = True):
    if is_test:
        test_input: str = """
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
                """
        test_lines = test_input.split("\n")
        return test_lines

    with open("1.txt") as file:
        return file.readlines()


def find_magic_numbers(lines: str) -> int:
    first: str = None
    last: str = None
    total: int = 0

    for line in lines:
        for c in line.strip():
            if c.isdigit():
                last = c
                if first is None:
                    first = c
        if (not first is None) and (not last is None):
            both: str = first + last
            print(both)
            total = total + int(both)
            first = None
            last = None

    return total


if __name__ == '__main__':
    data = read_input(False)
    print(find_magic_numbers(data))
