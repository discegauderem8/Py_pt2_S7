from random import randint as rnd, sample

def print_names(file_name, alphabet, vowels, number_of_names):
    with open(f"{file_name}", "a", encoding="UTF-8") as f:

        counter = 0
        while counter <= number_of_names:
            name_char = sample(alphabet, rnd(4, 10))
            if len(set(name_char) & set(vowels)) <= 0:
                continue
            name = "".join(name_char)
            f.write(name.title() + "\n")
            counter += 1





file_name="file.txt"
alphabet="а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я".replace(" ", "").split(",")
vowels = "а, я, у, ю, о, е, ё, э, и, ы".split(", ")
names_number = 10

print_names(file_name, alphabet, vowels, names_number)