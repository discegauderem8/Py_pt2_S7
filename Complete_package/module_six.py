from module_five import create_f_ext
from random import randint
import os


def create_files_n_dirs (path_to_new_dir, this_extension):
    if not os.path.exists(path_to_new_dir):
        os.mkdir(path_to_new_dir)
        create_f_ext(path=path_to_new_dir, nums_and_extensions=this_extension)
    else:
        while os.path.exists(path_to_new_dir):
            path_to_new_dir += str(randint(1,10))
        else:
            os.mkdir(path_to_new_dir)
            create_f_ext(path=path_to_new_dir, nums_and_extensions=this_extension)

create_files_n_dirs(path_to_new_dir="\some_dir", this_extension=((".txt",3),))