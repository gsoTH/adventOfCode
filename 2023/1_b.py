# https://adventofcode.com/2023/day/1
#
# On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# It looks like some of the digits are actually spelled out with letters
digit_words: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_words_sorted: list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_words_sorted.sort(key=len)


# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.
test_input: str = """
6three2sixsix9eightfour
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def read_input(is_test: bool = True):
    if is_test:
        test_lines = test_input.split("\n")
        return test_lines

    with open("1.txt") as file:
        return file.readlines()


def find_magic_numbers(lines: str) -> int:
    first: str = None
    last: str = None
    total: int = 0

    for line in lines:
        i: int = 0
        for c in line.strip():
            if c.isdigit():
                last = c
                if first is None:
                    first = c
                    continue    # Falls digit gefunden, muss nicht nach Worten gesucht werden.
            else:
                for word in digit_words_sorted:
                    #if i < len(word)-1:
                    #    break
                    start: int = i - (len(word)-2)
                    end: int = i + 2                               # a[start:stop]  items start through stop-1 <-- sehr komisch! :(
                    candidate: str = line.strip()[start:end]
                    if candidate == word:
                        number_value: int = digit_words.index(word) + 1
                        last = str(number_value)
                        if first is None:
                            first = str(number_value)
                            break
            i = i + 1

        if (not first is None) and (not last is None):
            both: str = first + last
            print(both + " " + line.strip())
            total = total + int(both)
            first = None
            last = None

    return total


if __name__ == '__main__':
    data = read_input(False)
    print(find_magic_numbers(data))
