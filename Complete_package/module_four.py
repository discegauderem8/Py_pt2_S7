import string
from random import randbytes, randint, sample

def create_files(extension=".txt", min_len=6, max_len=24, min_bytes=256, max_bytes=4096, num_of_files=42, pathname=""):
    for _ in range(num_of_files):
        name = "".join(sample(string.ascii_lowercase, randint(min_len, max_len-1)))
        this_abs_path = r"C:\Users\Александр\Desktop\Geek Brains\Python курс 2 практика\S7\004 and 005"
        path_n_name = f"{this_abs_path}{pathname}\\{name}{extension}"

        with open(path_n_name, "wb") as f:
            f.write(randbytes(randint(min_bytes, max_bytes)))

create_files(extension=".txt")
