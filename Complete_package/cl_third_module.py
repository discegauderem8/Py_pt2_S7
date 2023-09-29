from pathlib import Path

names_path = Path(r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\002\file.txt")
num_path = Path(r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\001\file.txt")
result_path = Path(r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\003\result.txt")

with (
    open(names_path, "r", encoding="utf-8") as names_file,
    open(num_path, "r", encoding="utf-8") as numbers_file,
    open(result_path, "w", encoding="utf-8") as result_file
):
    names = names_file.readlines()
    nums = numbers_file.readlines()

    nums = [int(x.strip().split("|")[0]) * float(x.strip().split("|")[1]) for x in nums]

    result = [(abs(num), name.lower()) if num <= 0 else (round(num), name.upper()) for num, name in zip(nums, names)]

    for item in result:
        result_file.write(str(item[0]).strip("\n") + ":" + str(item[1]) +"\n")


