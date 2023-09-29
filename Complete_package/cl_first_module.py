from random import randint as ri
from random import uniform as rnd
import os

file_name = "file.txt"


def print_to_file(file_path, number_of_lines):
    with open(f"{file_path}", "a", encoding="UTF-8") as f:
        f.writelines([f"{ri(-1000, 1001)} | {rnd(-1000.0, 1000.1)}" + "\n" for i in range(number_of_lines)])


print_to_file(file_name, 10)
