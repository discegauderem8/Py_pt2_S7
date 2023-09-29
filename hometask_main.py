from Hometask import *


directory = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\target_dir"
target_name = "UPDATED"
num_digits = 3
source_extension = ".txt"
target_extension = ".csv"
name_range = (3, 6)
if is_valid_directory(directory):
    rename_files(directory, target_name, num_digits, source_extension, target_extension, name_range)
else:
    print("Директории не существует.")