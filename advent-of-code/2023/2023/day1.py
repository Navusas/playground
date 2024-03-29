##########################################
## Task
##########################################
# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

##########################################
## Implementation
##########################################
def part1():
    with open('2023/day1-p1.input') as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        numbers = [int(x) for x in line if x.isdigit()]

        if len(numbers) > 0:
            answer = numbers[0].__str__()
        if len(numbers) > 1:
            answer += numbers[-1].__str__()
        else:
            answer += numbers[0].__str__()

        sum += int(answer)
        # print(f"Line: {line} - Numbers: {numbers}. Choosing {answer} - Sum: {sum}")
    print(f"Part 1 answer: {sum}")

##########################################
## Task
##########################################
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

##########################################
## Implementation
##########################################
def part2():
    """
    I am going to simply loop through a line, and then build a "matrix" of
    all the digits (letters or actual digits) I found, recording their indexes.
    
    Once it's done I will sort the matrix by the index, and then sum the first
    and last digit of the matrix.
    """
    with open('2023/day1-p2.input') as f:
        lines = f.read().splitlines()

    numbers_map = {
        "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
        "6": "6", "7": "7", "8": "8", "9": "9",
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    total_sum = 0
    for line in lines:
        line = line.strip()
        matrix = []
        print(f"Line: {line}")
        for num_word, digit in numbers_map.items():
            play_line = line
            while num_word in play_line:
                index_at = play_line.index(num_word)
                matrix.append([index_at, digit])
                play_line = play_line.replace(num_word, "", 1)
        
        matrix.sort(key=lambda x: x[0])
        matrix_sum = matrix_first_and_last_num_sum(matrix)
        print(f"- Matrix: {matrix} - Matrix Sum: {matrix_sum} - Total Sum: {total_sum}")
        total_sum += matrix_sum
    
    print(f"Part 2 answer: {total_sum}")


def matrix_first_and_last_num_sum(matrix):
    f_num_word, f_digit = matrix[0] if len(matrix) > 0 else ["0", "0"]
    _, l_digit = matrix[-1] if len(matrix) > 1 else [f_num_word, f_digit]

    return int(f_digit) * 10 + int(l_digit)

if __name__ == "__main__":
    print("Day 1: Trebuchet?!")
    part1()
    part2()